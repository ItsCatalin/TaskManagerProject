from django.urls import path
from . import views

urlpatterns = [
    #--------------------- Home Page -------------------------#
    path('', views.home, name=""),

    #--------------------- Dashboard -------------------------#
    path('dashboard', views.dashboard, name="dashboard"),

    #---------------------- Create Task ----------------------#

    path('createtask', views.createTask, name='createtask'),

    #--------------------- View Tasks ------------------------#

    path('taskview', views.taskView, name='taskview'),

    #--------------------- Update Task -----------------------#
    path('updatetask/<str:pk>/', views.updateTask, name='updatetask'),

    #--------------------- Update Task -----------------------#
    path('deletetask/<str:pk>/', views.deleteTask, name='deletetask'),
     

    #--------------------- User Registration -----------------#
    path('register', views.register, name="register"), 

    #---------------------- User Login -----------------------#
    path('login', views.my_login, name="login"), 

    #---------------------- User Logout ----------------------#
    path('logout', views.logout, name="logout"),
]

