from django.urls import path

from . import views
#access view file from this import

urlpatterns = [

    path('',views.home,name='home'),#Url for home page (view.home is file name) 
    # (anytime you create webpage you need URL like this and must create view and template with html file)
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('product/<int:pk>',views.product,name='product'),#pass int for pk (id)
    path('register/',views.register_user,name='register'),
    path('category/<str:food>/',views.category,name='category'),#pass string for category to be different 
    path('foods/', views.foods, name='foods'),
    path('update_user/',views.update_user,name='update_user'),
    path('update_info/',views.update_info,name='update_info'),

]