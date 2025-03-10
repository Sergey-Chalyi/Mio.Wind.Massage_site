# Generated by Django 5.1.4 on 2025-01-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_comment_specialist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ava_photo',
            field=models.ImageField(blank=True, upload_to='employees/', verbose_name='Фото для аватарки'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='card_photo',
            field=models.ImageField(blank=True, upload_to='employees/', verbose_name='Фото для карточки'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='main_photo',
            field=models.ImageField(blank=True, upload_to='employees/', verbose_name='Главное фото'),
        ),
    ]
