
from django.shortcuts import render
from django.urls import reverse_lazy
from.forms import CategoryRegistrationForm, LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,login as dj_login
from django.contrib.auth import logout as dca_logout
from django.shortcuts import render
from django.db.models import Q
from  .models import Category, Houselocation
from.forms import HouselocationRegistrationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=HouselocationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=HouselocationRegistrationForm()
              
    return render(request, 'index.html',{'form':form})    
    
    """Home page view."""

def list_houses(request):
        houses=Houselocation.objects.all()
        return render(request, 'housedisplay.html',{'houses':houses})



def register(request):
    """Registration view."""
    if request.method == 'GET':
        # executed to render the registration page
        register_form = RegisterForm()
        return render(request, 'register.html', locals())
    else:
        # executed on registration form submission
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            User.objects.create(
                first_name=request.POST.get('firstname'),
                last_name=request.POST.get('lastname'),
                email=request.POST.get('email'),
                username=request.POST.get('email'),
                password=make_password(request.POST.get('password'))
            )
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            print(register_form.errors)
        return render(request, 'register.html', locals())

def login(request):
    """Login view."""
    if request.method == 'GET':
        # executed to render the login page
        login_form = LoginForm()
        return render(request, 'login.html', locals())
    else:
        # get user credentials input
        username = request.POST['email']
        password = request.POST['password']
        # If the email provided by user exists and match the
        # password he provided, then we authenticate him.
        user = authenticate(username=username, password=password)
        if user is not None:
            # if the credentials are good, we login the user
            dj_login(request, user)
            # then we redirect him to home page
            return HttpResponseRedirect('/home')
        # if the credentials are wrong, we redirect him to login and let him know
        return render(
            request,
            'login.html',
            {
                'wrong_credentials': True,
                'login_form': LoginForm(request.POST)
            }
        )
def logout(request):
    """Logout view."""
    # logout the request
    dca_logout(request)
   
    # redirect user to home page
    return HttpResponseRedirect('/')




def searchcategory(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(categoryname__icontains=query) | Q(location__icontains=query)

            results=Category.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')




def agents_view(request):
    """agent page view."""
    if request.method == 'POST':
        form=HouselocationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=HouselocationRegistrationForm()
              
    return render(request, 'agents-grid.html',{'form':form})   
    

def property_view(request):
    """property page view."""
    if request.method == 'POST':
        form=HouselocationRegistrationForm(request.POST)
        theform=CategoryRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        if theform.is_valid():
            theform.save()    
    else:
        form=HouselocationRegistrationForm()
        theform=CategoryRegistrationForm()
    
    return render(request, 'property-grid.html',{'form':form,'theform':theform})     

    
   

        
                
    


def contacts_view(request):
    """contact page view."""
    if request.method == 'POST':
        form=HouselocationRegistrationForm(request.POST)
        theform=CategoryRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

        if theform.is_valid():
            theform.save()    
   
    else:
        form=HouselocationRegistrationForm()
        theform=CategoryRegistrationForm()
              
    return render(request, 'contact.html',{'form':form})   
              
        
          
   
def keja_view(request):
    """contact page view."""
    if request.method == 'POST':
        form=HouselocationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=HouselocationRegistrationForm()
    return render(request, 'property-single.html',{'form':form})   




	
