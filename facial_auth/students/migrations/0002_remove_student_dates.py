# Generated by Django 3.0.5 on 2021-08-15 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dates',
        ),
    ]