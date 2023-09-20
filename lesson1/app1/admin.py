from django.contrib import admin

# Register your models here.
from app1.models import Junior, Middle, Senior

admin.site.register(Junior)
admin.site.register(Middle)
admin.site.register(Senior)