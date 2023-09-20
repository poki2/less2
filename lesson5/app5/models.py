from django.db import models

# Create your models here.


class Car(models.Model):
    mark = models.CharField(max_length=355)
    years = models.IntegerField()
    color = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)

    def __str__(self):
        return f'{self.mark} - {self.price}'