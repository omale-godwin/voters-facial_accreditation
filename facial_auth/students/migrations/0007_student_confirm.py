# Generated by Django 3.0.5 on 2021-08-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20210815_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
