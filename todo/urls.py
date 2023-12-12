from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.my_login),
    path('', views.home),


#create tasks
    path('createtask', views.createTask, name='createtask'),

#view tasks

    path('viewtasks', views.ViewTasks, name='viewtasks'),

#update tasks

    path('updatetask/<str:pk>/', views.updateTask, name='updatetask'),

#Delete task
    path('deletetask/<str:pk>/', views.deleteTask, name='deletetask'),
]