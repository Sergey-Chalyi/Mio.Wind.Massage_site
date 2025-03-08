# Generated by Django 5.1.4 on 2025-01-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_visitrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва поля на сайті')),
                ('text', models.CharField(max_length=100, verbose_name='Назва поля на сайті')),
            ],
            options={
                'verbose_name': 'Блок: welcome',
            },
        ),
    ]
