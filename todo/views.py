from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm
from .forms import LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'index.html')


# Registering / Creating a  user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()   

            return HttpResponse("User registration was succesful!")
        
    context = {'form': form}

    return render(request, 'register.html', context=context)


#Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            #Checking if the user exists in the database
            if user is not None:
                
                auth.login(request, user)

                return redirect("dashboard")
            
    context = {'form': form}

    return render(request, 'login.html', context=context)



@login_required(login_url='login') #This decorator will only allow users on the dashboard page if they are logged in 
def dashboard(request):
    return render(request, "dashboard.html")



#log out a user
def logout(request):

    auth.logout(request)

    return redirect("")

    