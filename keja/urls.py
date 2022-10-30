from django.urls import path
from django.conf.urls.static import static
from .views import agents_view, contacts_view, index, keja_view, list_houses, login, property_view, register,searchcategory
from .views import logout
# from google import views as view


 
urlpatterns=[
    path('home',index,name='index'),
    path('',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('houses',list_houses,name='house'),
    path('property',property_view,name='property'),
    path('agents',agents_view,name='agent'),
    path('contact',contacts_view,name='contact'),
    path('kejainfo',keja_view,name='keja'),
    path('search', searchcategory, name='search'),
    

    

]