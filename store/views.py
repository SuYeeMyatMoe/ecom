from django.shortcuts import render

# Create your views here.
def home(request):#wanna pass the request in here
    return render(request,'home.html',{})#{} is empty context dictionary
    #home.html need to direct the template directiory in store app so create new folder (I named folder as templates to store all html templates)