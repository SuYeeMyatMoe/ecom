from django.shortcuts import render, redirect
from .models import Product, Category#import Product and Category models from Database
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages#to inform user with messages for errors
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


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
                messages.success(request, "You have successfully registered and logged in!")
                return redirect('home')
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