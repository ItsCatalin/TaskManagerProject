from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    date_poseted = models.DateField(auto_now_add=True)

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)

    reviewer_title = models.CharField(max_length=85)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)