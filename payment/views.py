from django.shortcuts import render, redirect
from cart.cart import Cart#access cart from this page
from decimal import Decimal
from .forms import DeliveryForm
from .models import DeliveryAddress, Order,OrderItem
from store.models import Product
from payment.forms import PaymentForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def payment_success(request):
    return render(request,"payment/payment_success.html",{})


def checkout(request):
    current_user = request.user
    cart = Cart(request)
    cart_products = cart.get_items()
    cart_quantity = cart.get_quants()

    # --- Calculate totals ---
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

    # --- Load form (with logged-in user’s saved address if available) ---
    if request.user.is_authenticated:
        delivery_address, created = DeliveryAddress.objects.get_or_create(user=current_user)
        form = DeliveryForm(request.POST or None, instance=delivery_address)
    else:
        form = DeliveryForm(request.POST or None)

    # --- Save delivery info ---
    if request.method == "POST" and form.is_valid():
        delivery = form.save(commit=False)
        if request.user.is_authenticated:
            delivery.user = current_user
        delivery.save()

        # Store delivery info in session
        request.session["my_delivery"] = {
            "full_name": delivery.full_name,
            "email": delivery.email,
            "deliver_address": delivery.deliver_address,
            "deliver_city": delivery.deliver_city,
            "deliver_state": delivery.deliver_state,
            "deliver_zipcode": delivery.deliver_zipcode,
        }

        request.session.modified = True  # make sure it's written

        messages.success(request, "Delivery information saved. Continue to billing.")
        return redirect("billing_info")

    return render(request, "payment/checkout.html", {
        "order_items": order_items,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "tax": tax,
        "cart_total": cart_total,
        "form": form,
    })


def billing_info(request):
    cart = Cart(request)
    cart_products = cart.get_items()
    cart_quantity = cart.get_quants()

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

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Save billing info in session for later order processing
            request.session["billing_info"] = form.cleaned_data
            return redirect("process_order")  # You can create a process_order view next
    else:
        form = PaymentForm()

    return render(request, "payment/billing_info.html", {
        "order_items": order_items,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "tax": tax,
        "cart_total": cart_total,
        "form": form,
    })

def process_order(request):
    cart = Cart(request)
    cart_products = cart.get_items()
    cart_quantity = cart.get_quants()

    subtotal = Decimal("0.00")
    for product in cart_products:
        qty = cart_quantity.get(str(product.id), 0)
        if product.is_sale:
            subtotal += Decimal(qty) * product.sale_price
        else:
            subtotal += Decimal(qty) * product.price

    delivery_fee = Decimal("5.00")
    tax_rate = Decimal("0.06")
    tax = (subtotal * tax_rate).quantize(Decimal("0.01"))
    cart_total = subtotal + delivery_fee + tax

    my_delivery = request.session.get("my_delivery")
    billing = request.session.get("billing_info")

    if not my_delivery or not billing:
        messages.error(request, "Missing delivery or billing information.")
        return redirect("checkout")

    full_name = my_delivery["full_name"]
    email = my_delivery["email"]
    delivery_address = (
        f"{my_delivery['deliver_address']}\n"
        f"{my_delivery['deliver_city']}\n"
        f"{my_delivery['deliver_state']}\n"
        f"{my_delivery['deliver_zipcode']}"
    )

    # Save order
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    create_order = Order.objects.create(
        user=user,
        full_name=full_name,
        email=email,
        address=delivery_address,
        amount_paid=cart_total
    )

    # Save order items
    for product in cart_products:
        qty = cart_quantity.get(str(product.id), 0)
        price = product.sale_price if product.is_sale else product.price
        OrderItem.objects.create(
            order=create_order,
            product=product,
            user=user,
            quantity=qty,
            price=price
        )

    messages.success(request, "Your order is successfully placed")
    return redirect("home")


