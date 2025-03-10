# Generated by Django 5.1.4 on 2025-01-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название абонемента')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/subscriptions/', verbose_name='Фото для карточки')),
                ('details', models.JSONField(verbose_name='Детали абонемента (длительность, цены, ссылки, фразы)')),
            ],
            options={
                'verbose_name': 'Массажная услуга',
                'verbose_name_plural': 'Массажные услуги',
            },
        ),
    ]
