from rest_framework import serializers
from .models import Machine, Attack, AttackResult

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = '__all__'

class AttackResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackResult
        fields = '__all__'
    