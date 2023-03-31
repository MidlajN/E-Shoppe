from django.db import models
from E_User.models import User
from E_App.models import Product


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    shipping_address = models.TextField(max_length=400)
    city = models.CharField(max_length=250, null=True)
    total_amount = models.IntegerField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_update = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Order'
        ordering = ['order_date']

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    seller = models.ForeignKey(User , null=True, on_delete=models.CASCADE)
    order_status = (
        ('pending','pending'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered'),
        ('cancel', 'cancel'),
    )
    status = models.CharField(max_length=250, choices=order_status, default='pending')

    class Meta:
        db_table = 'OrderItem'
        ordering = ['order']





