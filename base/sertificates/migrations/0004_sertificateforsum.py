# Generated by Django 5.1.4 on 2025-01-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertificates', '0003_subscription_photo_short_alter_subscription_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SertificateForSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/subscriptions/', verbose_name='Фото (нормальная по ширине)')),
                ('photo_short', models.ImageField(blank=True, null=True, upload_to='media/subscriptions/', verbose_name='Фото (для узких экранов)')),
                ('altedgio_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на отзывы Альтеджио')),
                ('phrase', models.CharField(max_length=255, verbose_name='Фраза')),
            ],
            options={
                'verbose_name': 'Сертификат на сумму',
                'verbose_name_plural': 'Сертификаты на суммы',
            },
        ),
    ]
