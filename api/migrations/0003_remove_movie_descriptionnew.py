# Generated by Django 4.1 on 2022-08-26 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_descriptionnew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='descriptionNew',
        ),
    ]