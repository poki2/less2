from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class MotherboardForm(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'


#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')
#
#
# class CustomUserChangeForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password1')
