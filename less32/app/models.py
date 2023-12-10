
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=255)
    quantity_in_stock = models.IntegerField()
    category = models.CharField(max_length=50, choices=[
        ('lightbulb', 'Lightbulb'),
        ('graphics_card', 'Graphics Card'),
        ('mixer', 'Mixer'),
    ])
    application_area = models.CharField(max_length=50, choices=[
        ('home', 'For Home'),
        ('kitchen', 'For Kitchen'),
        ('garden', 'For Garden'),
        ('clothing', 'Clothing'),
    ])
    date_added = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
