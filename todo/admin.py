from django.contrib import admin
from .models import Task

# We register our model task so we can see it on our admin page 
admin.site.register(Task)