# Generated by Django 5.1.4 on 2025-01-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_footerblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherPagesMainPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=100, verbose_name='Назва сторінки')),
                ('title', models.CharField(max_length=255, verbose_name='Фраза зверху сторінки')),
                ('photo', models.ImageField(upload_to='pictures/', verbose_name='Фото для верху сторінки')),
            ],
            options={
                'verbose_name': 'Фото для сторінки',
                'verbose_name_plural': 'Фото для сторінок',
            },
        ),
        migrations.AlterModelOptions(
            name='footerblock',
            options={'verbose_name': 'Блок: footer', 'verbose_name_plural': 'Блок: footer'},
        ),
    ]
