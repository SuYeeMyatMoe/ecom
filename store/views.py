from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product#import Product models from Database
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages#to inform user with messages for errors

# Create your views here.
def home(request):#wanna pass the request in here
#after importing, we will gonna use models in home page

    products= Product.objects.all()#get data from product models in dbs and output as variable
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
            login(request,user)
            messages.success(request, "You have successfully login!")
            return redirect('home')
        else:
            messages.success(request, "The login process is rejected, Please try again!")
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):    
    logout(request)
    messages.success(request,("You have successfully logout!"))
    return redirect('home')