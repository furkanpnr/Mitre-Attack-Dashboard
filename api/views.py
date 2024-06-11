from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Machine, Attack, AttackResult
from .serializers import MachineSerializer, AttackSerializer, AttackResultSerializer
from rich import print
import base64
from django.core.files.base import ContentFile
"""
api/v1/machine/
    get -> return all machine
    post -> create a machine
    delete -> delete all machine
    
api/v1/machine/{id}/
    get -> return the machine
    put -> update the machine
    delete -> delete the machine

api/v1/attack/
    get -> return all attack
    post -> create a attack
    delete -> delete all attack

api/v1/attack/{id}/
    get -> return the attack
    put -> update the attack
    delete -> delete the attack
    
api/v1/attack-result/
    get -> return all attack-result
    post -> create a attack-result
    delete -> delete all attack-result

api/v1/attack-result/{id}/
    get -> return the attack-result
    put -> update the attack-result
    delete -> delete the attack-result
    
    
result: 
    {
        "success": True,
        "executed_date": datetime.now(),
        "machine": SystemInfo._get_mac_addr(),
        "attack": MitreAttack.SCREEN_CAPTURE.value,
        "data":  {
            "img_binary_data": buffer.getvalue()
        }
    }

"""

# Machine Views
class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    

class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    lookup_field = "id"

# Attack Views
class AttackListCreateView(generics.ListCreateAPIView):
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer

class AttackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer
    lookup_field = "id"

# AttackResult Views
class AttackResultListCreateView(generics.ListCreateAPIView):
    queryset = AttackResult.objects.all()
    serializer_class = AttackResultSerializer
    
    def create(self, request, *args, **kwargs):
        body = request.data
        result_type = body.get('result_type')
        
        try:
            machine = Machine.objects.get(mac_addr=body.get('machine'))
            attack = Attack.objects.get(mitre_id=body.get('attack'))
        except Machine.DoesNotExist:
            return Response({"error": "Machine not found"}, status=status.HTTP_404_NOT_FOUND)
        except Attack.DoesNotExist:
            return Response({"error": "Attack not found"}, status=status.HTTP_404_NOT_FOUND)
                
    
        data_fields = body.get('data', {})
        image_file = None

        if result_type == 'screen_capture':
            image_data = data_fields.get('image_binary')
            if not image_data:
                return Response({"error": "Image data is required for screen capture result"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                image_binary = base64.b64decode(image_data)
                image_file = ContentFile(image_binary, name=f"{machine.mac_addr}_{body.get('executed_date')}.png")
            except Exception as e:
                return Response({"error": "Invalid image data"}, status=status.HTTP_400_BAD_REQUEST)

        
        attack_result = AttackResult(
            result_type=result_type,
            success=body.get('success'),
            executed_date=body.get('executed_date'),
            machine=machine,
            attack=attack,
            image=image_file,
            data=data_fields
        )
        
        attack_result.save()
        serializer = self.get_serializer(attack_result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
 
class AttackResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttackResult.objects.all()
    serializer_class = AttackResultSerializer
    lookup_field = "id"