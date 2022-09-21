from django.urls import path
from django.conf.urls.static import static
from .views import index, login, register
from .views import logout

 
urlpatterns=[
    path('',index,name='index'),
     path('register',register,name='register'),
     path('login',login,name='login'),
     path('logout',logout,name='logout')
]