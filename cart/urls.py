from django.urls import path
from . import views
#access view file from this import

urlpatterns = [
    #for summary,add,remove,update and will control with js ajex
    path('',views.cart_summary, name="cart_summary"),
    path('add/',views.cart_add, name="cart_add"),
    path('delete/',views.cart_delete, name="cart_delete"),
    path('update/',views.cart_update, name="cart_update"),
]