from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.form import *
from app.models import *

# Register your models here.
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(HDD)
admin.site.register(SSD)
admin.site.register(GraphicsCard)
admin.site.register(Cooler)
admin.site.register(ComputerCase)
admin.site.register(Processor)
admin.site.register(PowerSupply)


