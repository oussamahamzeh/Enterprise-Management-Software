# Generated by Django 2.2 on 2023-05-07 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0008_auto_20230507_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='code',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='purchase_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='selling_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='selling_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.Client'),
        ),
    ]
