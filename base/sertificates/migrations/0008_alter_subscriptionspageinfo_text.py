# Generated by Django 5.1.4 on 2025-01-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertificates', '0007_subscriptionspageinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionspageinfo',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]
