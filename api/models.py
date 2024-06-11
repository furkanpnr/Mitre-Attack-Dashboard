from django.db import models
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
import base64

# Create your models here.
class Machine(models.Model):
    public_ip = models.CharField(max_length=20, blank=True)
    local_ip = models.CharField(max_length=20, blank=True)
    mac_addr = models.CharField(max_length=30, blank=True, unique=True)
    os_name = models.CharField(max_length=50, blank=True)
    os_version = models.CharField(max_length=500, blank=True)
    os_arch = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=50, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user_name} ({self.public_ip})'

class Attack(models.Model):
    mitre_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
  
    def __str__(self):
        return self.name

class AttackResult(models.Model):
    RESULT_TYPES = [
        ('screen_capture', 'Screen Capture'),
        ('system_info', 'System Info'),
        ('clipboard_data', 'Clipboard Data'),
    ]
    result_type = models.CharField(max_length=50, choices=RESULT_TYPES)
    success = models.BooleanField()
    executed_date = models.DateTimeField(null=True, )
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='attack_results')
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name='attack_results')
    data = models.JSONField(null=True, blank=True)
    image = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.result_type == 'screen_capture' and self.data:
            image_data = self.data.get('image_binary')
            if image_data:
                image = Image.open(BytesIO(base64.b64decode(image_data)))
                image_io = BytesIO()
                image.save(image_io, format='PNG')
                self.image.save(f'{self.machine.mac_addr}_{self.executed_date}.png', ContentFile(image_io.getvalue()), save=False)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.result_type.title()} Result -- {self.machine.mac_addr} -- {self.executed_date.isoformat()}"
