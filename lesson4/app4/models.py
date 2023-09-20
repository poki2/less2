from django.db import models

# Create your models here.


class Foo(models.Model):
    userId = models.IntegerField()
    _id = models.IntegerField()
    title = models.CharField(max_length=50)
    completed = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.userId} - {self._id} - {self.title} - {self.completed}'