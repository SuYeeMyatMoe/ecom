from django.contrib import admin
from .models import Category,Customer,Product,Order #import the model after migration

# After import model in above, register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)


