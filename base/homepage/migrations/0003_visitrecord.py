# Generated by Django 5.1.4 on 2025-01-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_privacypolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now=True, verbose_name='Час створення запису')),
                ('customer_name', models.CharField(max_length=100, verbose_name="Ім'я клієнта")),
                ('customer_tel', models.CharField(max_length=100, verbose_name='Номер клієнта')),
                ('customer_comment', models.TextField(blank=True, max_length=1000, verbose_name='Кментар клієнта')),
                ('to_specialist', models.CharField(blank=True, max_length=100, verbose_name='До спеціаліста')),
                ('servise_name', models.CharField(blank=True, max_length=100, verbose_name='Назва послуги')),
                ('servise_duration', models.CharField(blank=True, max_length=100, verbose_name='Тривалість послуги')),
                ('servise_count', models.CharField(blank=True, max_length=100, verbose_name='Кількість послуг')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Чи клієнт обслугован?')),
            ],
            options={
                'verbose_name': 'Запис клієнта',
                'verbose_name_plural': 'Записи клієнтів',
            },
        ),
    ]
