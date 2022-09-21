
from django.shortcuts import render
from.forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as dca_logout
# Create your views here.
def index(request):
    """Home page view."""
    return render(request, 'index.html')
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
            return HttpResponseRedirect('/login')
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
            login(request, user)
            # then we redirect him to home page
            return HttpResponseRedirect('/')
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

