# Generated by Django 5.1.4 on 2025-01-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/employees/', verbose_name='Фото'),
        ),
    ]
