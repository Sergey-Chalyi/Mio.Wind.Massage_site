# Generated by Django 5.1.4 on 2025-01-22 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_employeesinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeesInfo',
            new_name='EmployeesPageInfo',
        ),
    ]
