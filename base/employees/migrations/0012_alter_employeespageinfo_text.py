# Generated by Django 5.1.4 on 2025-01-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_rename_employeesinfo_employeespageinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeespageinfo',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
