from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser, Order


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('avatar', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('username', 'address', 'phone_number')

