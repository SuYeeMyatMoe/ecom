from django.shortcuts import render
from cart.cart import Cart#access cart from this page
from decimal import Decimal
from store.forms import UserInfoForm
from store.models import Profile   
from store.models import Product

# Create your views here.
def payment_success(request):
    return render(request,"payment/payment_success.html",{})

def checkout(request):
    current_user = request.user
    cart = Cart(request)
    cart_products = cart.get_items()   # call the method
    cart_quantity = cart.get_quants()  # call the method

    order_items = []
    subtotal = Decimal("0.00")  

    for product in cart_products:
        qty = cart_quantity.get(str(product.id), 0)
        if product.is_sale:
            line_total = Decimal(qty) * product.sale_price
        else:
            line_total = Decimal(qty) * product.price
        subtotal += line_total

        order_items.append({
            "product": product,
            "qty": qty,
            "line_total": line_total,
        })

    delivery_fee = Decimal("5.00")  
    tax_rate = Decimal("0.06")      
    tax = (subtotal * tax_rate).quantize(Decimal("0.01"))
    cart_total = subtotal + delivery_fee + tax

    if request.user.is_authenticated:
        #Check out as login user
        profile, created = Profile.objects.get_or_create(user=current_user)
        form = UserInfoForm(request.POST or None, instance=profile)
        return render(request, "payment/checkout.html", {
        "order_items": order_items,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "tax": tax,
        "cart_total": cart_total,
        "form": form, 
    })
    else:
        #checkout ass guest
        form = UserInfoForm(request.POST or None)
        return render(request, "payment/checkout.html", {
        "order_items": order_items,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "tax": tax,
        "cart_total": cart_total,
        "form": form, 
    })


