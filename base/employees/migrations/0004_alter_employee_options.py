# Generated by Django 5.1.4 on 2025-01-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_employee_photo_employee_ava_photo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Співробітник', 'verbose_name_plural': 'Співробітники'},
        ),
    ]
