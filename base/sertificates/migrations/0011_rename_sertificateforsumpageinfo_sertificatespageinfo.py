# Generated by Django 5.1.4 on 2025-01-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sertificates', '0010_rename_comment_sertificateforsumpageinfo_comment_for_sum_sertificate_and_more'),
        ('servises', '0004_alter_service_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SertificateForSumPageinfo',
            new_name='SertificatesPageinfo',
        ),
    ]
