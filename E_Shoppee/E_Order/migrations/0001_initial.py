# Generated by Django 4.1.6 on 2023-03-17 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('E_App', '0002_product_seller'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('shipping_address', models.TextField(max_length=400)),
                ('city', models.CharField(max_length=250, null=True)),
                ('total_amount', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='pending', max_length=250)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_update', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['order_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Order.order')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_App.product')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'OrderItem',
                'ordering': ['order'],
            },
        ),
    ]