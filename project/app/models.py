from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return {self.name}



class Motherboard(models.Model):
    title = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    text = models.TextField()
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)



    def __str__(self):
        return f'{self.title} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Motherboard, self).save(*args, **kwargs)



class Video_card(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    text = models.TextField()
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Video_card, self).save(*args, **kwargs)


class CPU(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    kernels = models.IntegerField()
    
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kernels)
        super(CPU, self).save(*args, **kwargs)


class SSD(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    memory = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.memory)
        super(SSD, self).save(*args, **kwargs)

class HDD(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    memory = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(HDD, self).save(*args, **kwargs)


class Cooler(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    text = models.TextField()
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Cooler, self).save(*args, **kwargs)


class RAM(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='img/', null=True)
    price = models.PositiveIntegerField()
    memory = models.CharField(max_length=255)
    purity = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.memory)
        super(RAM, self).save(*args, **kwargs)