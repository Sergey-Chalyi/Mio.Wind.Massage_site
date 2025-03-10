# Generated by Django 5.1.4 on 2025-01-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0018_rename_time_addited_employee_time_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редагування'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редагування'),
        ),
    ]
