from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.db import models
from app.models import *

# Register your models here.
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(SSD)
admin.site.register(HDD)
admin.site.register(GraphicsCard)
admin.site.register(Cooler)
admin.site.register(ComputerCase)
admin.site.register(PowerSupply)
admin.site.register(Processor)
# admin.site.register(CustomUser)
#
# class CustomLogEntry(LogEntry):
#     custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='custom_logs')
#
# admin.site.register(CustomLogEntry)