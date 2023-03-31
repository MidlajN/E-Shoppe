# Generated by Django 4.1.6 on 2023-03-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Order', '0002_remove_order_status_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancel', 'cancel')], default='pending', max_length=250),
        ),
    ]
