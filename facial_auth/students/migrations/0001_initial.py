# Generated by Django 3.0.5 on 2021-08-15 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('emailA', models.EmailField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('states', models.CharField(max_length=200)),
                ('contry', models.CharField(max_length=200)),
                ('local_government', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('Imag', models.ImageField(upload_to='photos')),
                ('dates', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
