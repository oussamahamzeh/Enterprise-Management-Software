# Generated by Django 2.2 on 2023-05-07 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_auto_20230507_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='code',
        ),
        migrations.RemoveField(
            model_name='item',
            name='purchase_cost',
        ),
        migrations.RemoveField(
            model_name='item',
            name='selling_price',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='selling_price',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='client',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='Inventory.Client'),
            preserve_default=False,
        ),
    ]
