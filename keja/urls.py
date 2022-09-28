from django.urls import path
from django.conf.urls.static import static
from .views import index, list_houses, login, register
from .views import logout
# from google import views as view


 
urlpatterns=[
    path('',index,name='index'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
     path('houses',list_houses,name='house'),

    # path('search', searchcategory, name='search'),
    

    

]