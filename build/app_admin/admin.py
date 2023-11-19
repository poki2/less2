from django.contrib import admin

from app_admin.models import *

# Register your models here.
admin.site.register(ComputerCase)
admin.site.register(PowerSupply)
admin.site.register(Cooler)
admin.site.register(GraphicsCard)
admin.site.register(HDD)
admin.site.register(SSD)
admin.site.register(RAM)
admin.site.register(Processor)
admin.site.register(Motherboard)

