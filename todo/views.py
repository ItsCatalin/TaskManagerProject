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

#update a task

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('viewtasks')
    
    context = {'form': form}

    return render(request, 'updatetask.html', context=context)


#delete a task

def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()

        return redirect('viewtasks')

    contex = {"object": task}

    return render(request, 'deletetask.html', context=contex)
    
    