# Generated by Django 4.2.7 on 2023-11-21 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motherboard',
            name='slug',
        ),
    ]
