# Generated by Django 2.2 on 2023-08-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0017_transaction_tva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
