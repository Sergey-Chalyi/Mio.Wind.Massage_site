# Generated by Django 5.1.4 on 2025-01-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Політика конфіденційності')),
            ],
            options={
                'verbose_name': 'Політика конфіденційності',
                'verbose_name_plural': 'Політика конфіденційності',
            },
        ),
    ]
