
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms


#Register a user
class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']



#Log in a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())