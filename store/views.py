from django.shortcuts import render
from .models import Product#import Product models from Database

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