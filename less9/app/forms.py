from django import forms
from .models import Visitor

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'
