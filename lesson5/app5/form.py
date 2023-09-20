from django import forms

from app5.models import Car


class CarForm(forms.Form):
    class Meta:
        model = Car
        fields = {'mark', 'years', 'color', 'mileage', 'price'}