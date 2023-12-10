# models.py
from django.db import models

class Bottle(models.Model):
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"Bottle - Quantity: {self.quantity}"

class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order - Client: {self.client}, Date: {self.date_ordered}"

class CompletedOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Completed Order - Order: {self.order}, Date: {self.date_completed}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return f"Employee - Name: {self.name}, Busy: {self.busy}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"Client - Name: {self.name}"

class Revenue(models.Model):
    date = models.DateField()
    day_revenue = models.FloatField(default=0)
    week_revenue = models.FloatField(default=0)
    month_revenue = models.FloatField(default=0)


    def __str__(self):
        return f"Revenue - Date: {self.date}, Day: {self.day_revenue}, Week: {self.week_revenue}, Month: {self.month_revenue}"
