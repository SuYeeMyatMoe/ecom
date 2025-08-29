from .cart import Cart#import form cart.py

#create context processor so our cart will work in all pages
def cart(request):
    #Return the default data form our cart
    return {'cart':Cart(request)}