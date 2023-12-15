from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm
from .forms import LoginForm
from .forms import CreateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from .models import Task




def home(request):
    return render(request, 'index.html')


# Registering / Creating a  user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()   

            return redirect('dashboard')
        
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
    return render(request, "profile/dashboard.html")


#Create a task
@login_required(login_url='login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user #This will link the task to the user

            task.save()
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'profile/createtask.html', context=context)

#View all tasks
@login_required(login_url='login')
def taskView(request):

    current_user = request.user.id #This variable will get the user id
    task = Task.objects.all().filter(user=current_user)#This line will tak the tasks associated with the user id(the one that is logged in right now)

    context = {'task': task}

    return render(request, 'profile/taskview.html', context=context)
    

#update a task
@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)#If I want to update a task I will update that instance

    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskview')
        
    context = {'form': form}
    return render(request, 'profile/updatetask.html', context=context)

#delete a task
@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()

        return redirect('taskview')
    
    return render(request, 'profile/deletetask.html')
    


#log out a user
def logout(request):

    auth.logout(request)

    return redirect("")

    