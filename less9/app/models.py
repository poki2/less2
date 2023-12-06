from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    occupation = models.CharField(max_length=100)
    interests = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=20, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    preferred_os = models.CharField(max_length=20, choices=[('windows', 'Windows'), ('mac', 'Mac'), ('linux', 'Linux')])
    programming_languages = models.CharField(max_length=255)
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
