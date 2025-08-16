from django.db import models
import datetime# to know the date time and order 

# Models are in here
#Category
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name_plural= "categories"#line is just a display label setting to change something under its class (made by daverobb2011)

#Customer    
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.email} {self.password}'

#Product    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)#can get till 100k 
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    #need to download pillow (python image library) to upload images

    #Add Sale Stuff
    

    def __str__(self):
        return self.name

#Customer Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=255,default='',blank=False)
    phone = models.CharField(max_length=15,default='',blank=False)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)  # False = Pending, True = Completed

    def __str__(self):
        return self.product
    

    #make migration in terminal with this line (after cd and local )
    #  python manage.py makemigrations

    #migration folder is created so will create a migration with terminal again
    #python manage.py migrate (OK is replied so it works)

    #SuYeeMyatMoe
# suyeemyatmoe21@gmail.com
# 8000#2003
#the login credential for admin

# http://localhost:8000/admin (if we use this no need to login)