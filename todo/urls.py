from django.urls import path
from . import views

urlpatterns = [
    #--------------------- Home Page -------------------------#
    path('', views.home, name=""),

    #--------------------- Dashboard -------------------------#
    path('dashboard', views.dashboard, name="dashboard"),

    #--------------------- User Registration -----------------#
    path('register', views.register, name="register"), 

    #---------------------- User Login -----------------------#
    path('login', views.my_login, name="login"), 

    #---------------------- User Logout ----------------------#
    path('logout', views.logout, name="logout"),
]

