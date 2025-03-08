# Generated by Django 5.1.4 on 2025-01-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_aboutasblock_photo_full_aboutasblock_photo_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=100, verbose_name='Текст')),
                ('icon', models.FileField(upload_to='blocks/', verbose_name='Іконка')),
            ],
            options={
                'verbose_name': 'Блок: general benefits',
                'verbose_name_plural': 'Блок: general benefits',
            },
        ),
    ]
