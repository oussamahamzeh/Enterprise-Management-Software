# Generated by Django 4.2.9 on 2024-02-06 17:28

import Documents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0020_alter_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=Documents.models.document_upload_to),
        ),
    ]
