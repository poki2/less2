from django.contrib import admin

from app.models import *

# Register your models here.
admin.site.register(Bottle)
admin.site.register(Order)
admin.site.register(CompletedOrder)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Revenue)