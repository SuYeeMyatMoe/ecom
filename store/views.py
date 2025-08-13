from django.shortcuts import render
from .models import Product#import Product models from Database

# Create your views here.
def home(request):#wanna pass the request in here
    return render(request,'home.html',{})#{} is empty context dictionary
    #home.html need to direct the template directiory in store app so create new folder (I named folder as templates to store all html templates)
    # the running will stop if terminal is close
    #if there is no error, can run in localhost:8000

    #In store must have at least 4 model for dbs
    #category
    #product
    #cus
    #order