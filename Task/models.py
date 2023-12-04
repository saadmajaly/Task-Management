from django.db import models

# Create your models here.
class Task(models.Model):
 taskTitle=models.CharField(max_length=50)
 dueDate=models.DateField()
 taskDescription=models.TextField(max_length=250)