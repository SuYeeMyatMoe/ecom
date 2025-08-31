from django.urls import path

from . import views
#access view file from this import

urlpatterns = [

    path('payment_success',views.payment_success,name='payment_success'),#Url for home page (view.home is file name) 
    

]