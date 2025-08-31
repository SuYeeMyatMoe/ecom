from django.urls import path

from . import views
#access view file from this import

urlpatterns = [

    path('payment_success',views.payment_success,name='payment_success'),
    path('checkout',views.checkout,name='checkout'),
]