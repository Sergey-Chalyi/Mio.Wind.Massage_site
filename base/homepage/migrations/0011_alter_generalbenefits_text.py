# Generated by Django 5.1.4 on 2025-01-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_generalbenefits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalbenefits',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
