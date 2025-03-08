# Generated by Django 5.1.4 on 2025-01-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertificates', '0014_alter_sertificateforsum_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sertificateforsum',
            options={'verbose_name': 'Картка: сертифікат на суму', 'verbose_name_plural': 'Картки: cертифікати на суму'},
        ),
        migrations.AlterModelOptions(
            name='sertificatespageinfo',
            options={'verbose_name': 'Секція: сертифікати', 'verbose_name_plural': 'Секція: сертифікати'},
        ),
        migrations.AlterField(
            model_name='subscription',
            name='counts',
            field=models.JSONField(verbose_name='Види абонементів по кількості (JSON)'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='durations',
            field=models.JSONField(verbose_name='Види абонементів по тривалості (JSON)'),
        ),
    ]
