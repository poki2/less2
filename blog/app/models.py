from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=50)
    likes = models.IntegerField()

    def __str__(self):
        return f"{self.author} - {self.title}"

    def get_absolute_url(self):
        return reverse('blog', args=(self.pk, ))