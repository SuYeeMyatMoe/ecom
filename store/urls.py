from django.urls import path

from . import views
#access view file from this import

urlpatterns = [

    path('',views.home,name='home'),#Url for home page (view.home is file name) 
    # (anytime you create webpage you need URL like this and must create view and template with html file)
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout')
]