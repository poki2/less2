from django.contrib.auth.models import User
from django.db import models

from app.models import *


# Create your models here.


class CustomUser(User):
    user_email = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.username




class Order(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Order #{self.id} - {self.username}"