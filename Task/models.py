from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryColor = models.CharField(max_length=8, default="#FFFFFF")


class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    dueDate = models.DateField()
    taskDescription = models.TextField(max_length=250)
    taskPriority = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
