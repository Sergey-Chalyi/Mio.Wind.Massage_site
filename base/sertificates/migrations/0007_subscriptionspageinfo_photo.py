# Generated by Django 5.1.4 on 2025-01-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertificates', '0006_subscriptionspageinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionspageinfo',
            name='photo',
            field=models.FileField(blank=True, upload_to='backgrounds/', verbose_name='Фото для фону'),
        ),
    ]
