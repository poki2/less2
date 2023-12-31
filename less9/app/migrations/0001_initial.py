# Generated by Django 4.2.8 on 2023-12-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('occupation', models.CharField(max_length=100)),
                ('interests', models.CharField(max_length=255)),
                ('experience_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
                ('preferred_os', models.CharField(choices=[('windows', 'Windows'), ('mac', 'Mac'), ('linux', 'Linux')], max_length=20)),
                ('programming_languages', models.CharField(max_length=255)),
                ('additional_comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
