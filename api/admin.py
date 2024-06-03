from django.contrib import admin
from .models import Machine, Attack, AttackResult
# Register your models here.
admin.site.register(Machine)
admin.site.register(Attack)
admin.site.register(AttackResult)