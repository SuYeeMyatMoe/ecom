from django.db import models
import datetime# to know the date time and order 
from django.contrib.auth.models import User#login with django auth model
from django.db.models.signals import post_save#automactically create profile model with signal

# Models are in here
class Profile(models.Model):
    #associate this model with django auth user model
    user=models.OneToOneField(User, on_delete=models.CASCADE)#one profile with one user 
    # (when they delete their profile, they delete associate profile)
    date_motified= models.DateTimeField(User, auto_now=True)#to know when they modify the info
    phone=models.CharField(max_length=20,blank=True)#to be able to add many char like + and space
    address1=models.CharField(max_length=200,blank=True)
    address2= models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    state=models.CharField(max_length=200,blank=True)
    zipcode=models.CharField(max_length=200,blank=True)
    old_cart=models.CharField(max_length=200,blank=True,null=True)#will convert python dictionary shopping cart to a string

    def __str__(self):
        return self.user.username
    
#create a user profile by default when they register
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()#save the created profile

#automate the profile thing
post_save.connect(create_profile,sender=User) 
#python manage.py makemigrations
# python manage.py migrate           

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

    #Add Sale Stuff(hey, is this thing on sale yes or no)
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=6)#same as upper price
    #this is major change so must push migration in dbs

#python manage.py makemigrations
#python manage.py migrate
#if run the server and in admin panel, we can see the two input and we can make the sale price is different from real price
    

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