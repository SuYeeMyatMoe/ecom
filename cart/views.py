from django.shortcuts import render, get_object_or_404 # look up product and give 404 if there is none
from .cart import Cart#access cart from this page
from store.models import Product#access product from store model
from django.http import JsonResponse#json response

# Create your views here.
def cart_summary(request):
    return render(request,"cart_summary.html",{})

def cart_add(request):
    #get the cart
    cart=Cart(request)
    #test for POST
    if request.POST.get('action')=='post':#post is from each product page js jquery action 
        #Get Stuff
        product_id=int(request.POST.get('product_id'))
        #lookup product in DB
        product=get_object_or_404(Product,id=product_id)

        #save to session
        cart.add(product=product)

        #get cart quantity
        cart_quantity=cart.__len__()#access from cart.py request

        #Return response
        #response =JsonResponse({'Product Name: ':product.name})#will reference with product name (only for testing)
        response =JsonResponse({'qty':cart_quantity})#return quantity
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass