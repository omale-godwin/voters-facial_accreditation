# Generated by Django 3.0.5 on 2021-08-15 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_reg_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Imag',
            new_name='imag',
        ),
    ]
