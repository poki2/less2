from django import forms

from app.models import Product


class ProductCreate(forms.ModelForm):
    class Meta:
        fields =('title', 'photo', 'text', 'price', 'categories')
        model = Product