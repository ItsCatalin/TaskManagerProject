from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm








def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')


def my_login(request):
    return render(request, 'login.html')

def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('viewtasks')
    

    context = {'form': form}

    return render(request, 'createtask.html', context=context)


def ViewTasks(request):

    tasks = Task.objects.all()
    
    context = {'tasks': tasks}

    return render(request, 'viewtasks.html', context=context)