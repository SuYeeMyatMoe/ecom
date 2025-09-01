from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class DeliveryAddress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    address=models.TextField(max_length=250)
    city=models.TextField(max_length=250,null=True,blank=True)
    state=models.TextField(max_length=250,null=True,blank=True)
    zipcode=models.TextField(max_length=250)

    #don't pluralize address
    class Meta:
        verbose_name_plural="Delivery Address"

    def __str__(self):
        return f'Delivery Address - {str(self.id)}'


#create order model
class Order(models.Model):
    #Foreign key
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    address=models.TextField(max_length=250)
    amount_paid=models.DecimalField(max_digits=6, decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'


#create order item model
class OrderItem(models.Model):
    #Foreign key
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    quantity=models.PositiveBigIntegerField(default=1)#at least 1
    price=models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f'Order Item - {str(self.id)}'