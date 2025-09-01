from django.shortcuts import render, redirect
from .models import Product, Category#import Product and Category models from Database
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages#to inform user with messages for errors
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, UserInfoForm
from payment.forms import DeliveryForm# from payment forms.py
from payment.models import DeliveryAddress#from payment model.p file
from django import forms
from django.core.paginator import Paginator
import json
from cart.cart import Cart


# Create your views here.
def home(request):#wanna pass the request in here
#after importing, we will gonna use models in home page

    # products= Product.objects.all()#get data from product models in dbs and output as variable
    #wil only get all for food product page
    products = Product.objects.order_by('-id')[:4]  # latest 4
    return render(request,'home.html',{'products':products})#added model in context dictionary{} 
    #home.html need to direct the template directiory in store app so create new folder (I named folder as templates to store all html templates)
    # the running will stop if terminal is close
    #if there is no error, can run in localhost:8000

    #In store must have at least 4 model for dbs
    #category
    #product
    #cus
    #order

def about(request):    
    return render(request,'about.html',{})

def login_user(request):   
    if request.method=="POST":
        username=request.POST['user_name']#used name in input and we use that name in here 
        password=request.POST['userpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:#if login success, we let them login
            login(request,user)#login builtin function 

            #do shopping cart stuff
            #get current user
            current_user=Profile.objects.get(user__id=request.user.id)
            #get their saved cart from dbs
            saved_cart=current_user.old_cart

            #convert dbs string to python dictionary
            if saved_cart:# there is something in cart

                #convert to dic using json (because json convert str to dic very easily)
                converted_cart=json.loads(saved_cart)
                #add loaded cart dic to session

                #get cart
                cart=Cart(request)#from Cart class model in cart.py
                for key,value in converted_cart.items():#loop through the cart dic items and add items from dbs
                    cart.db_add(product=key,quantity=value)#must create db_add in cart.py to get them


            messages.success(request, "You have successfully login!")
            return redirect('home')
        else:
            messages.success(request, "The login process is rejected, Please try again!")
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):    
    logout(request)
    messages.success(request,("You have successfully logout the account!"))
    return redirect('home')

def product(request, pk):  
    product = Product.objects.get(id=pk)  # use singular name
    return render(request, 'product.html', {'product': product})

def register_user(request):    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #log in user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Your profile is successfully created, Please also fill delivery info in below!")
                return redirect('update_info')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})#pass form data

def category(request,food):#pass request and food
    #replace Hyphens with spaces
    food=food.replace('-',' ')
    #grab category from URL (look up category in dbs)
    try:
        #look up the category that is named with food in Category model
        category=Category.objects.get(name=food)
        products= Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
         messages.success(request, ("This category doesn't exist!"))
         return redirect('home')
    
def foods(request):
    product_list = Product.objects.all().order_by('-id')   # show all products
    paginator = Paginator(product_list, 12)  # 12 products per page
    
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    return render(request, 'foods.html', {'products': products})    

def update_user(request):
    if request.user.is_authenticated:  # only logged-in users can update
        current_user = request.user
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('home')

        return render(request, 'update_user.html', {'user_form': user_form})

    else:
        messages.error(request, "Please login to update your profile.")
        return redirect('login')  # better to send them to login instead of home

    
def update_info(request):
    if request.user.is_authenticated:
        current_user = request.user
        profile, created = Profile.objects.get_or_create(user=current_user)

        # FIX: Use filter().first() so it doesn't throw error if DeliveryAddress doesn't exist
        delivery_user = DeliveryAddress.objects.filter(user=current_user).first()

        # If no DeliveryAddress exists, create one linked to user
        if not delivery_user:
            delivery_user = DeliveryAddress.objects.create(user=current_user)

        form = UserInfoForm(request.POST or None, instance=profile)
        delivery_form = DeliveryForm(request.POST or None, instance=delivery_user)

        if request.method == "POST":
            if form.is_valid() and delivery_form.is_valid():
                form.save()
                delivery_form.save()
                messages.success(request, "Your profile and delivery info have been updated!")
                return redirect('home')

        return render(request, 'update_info.html', {
            'form': form,
            'delivery_form': delivery_form
        })

    else:
        messages.error(request, "Please login to update your delivery info.")
        return redirect('login')

