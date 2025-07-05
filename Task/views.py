from datetime import datetime, date
from django.shortcuts import redirect, render
from django.http import HttpResponse

import users
from .models import Task
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def Default_Redirect(request):

    return redirect("/tasks/0")


def home(request, sort):
    if request.user.is_authenticated:
        userId = request.user.id
    else:
        return render(request, "login.html", {"loginerror": "Please login first"})

    if sort == 0:
        tasks = Task.objects.filter(user=userId).order_by("taskPriority", "dueDate")
    if sort == 5:
        tasks = Task.objects.filter(user=userId).order_by("-taskPriority", "dueDate")
    if sort == 1:
        tasks = Task.objects.filter(user=userId).order_by("dueDate")
    if sort == 2:
        tasks = Task.objects.filter(user=userId).order_by("-dueDate")
    if sort == 3:
        tasks = Task.objects.filter(user=userId).order_by("taskTitle")
    if sort == 4:
        tasks = Task.objects.filter(user=userId).order_by("-taskTitle")
    return render(request, "Task/index.html", {"tasks": tasks})


def addtemp(request):

    return render(request, "Task/add.html")


@csrf_exempt
def add(request):
    title = request.POST["title"]
    date = request.POST["date"]
    description = request.POST["desc"]
    priority = request.POST["prio"]
    user = request.user
    task = Task(
        taskTitle=title,
        dueDate=date,
        taskDescription=description,
        taskPriority=priority,
        user=user,
    )
    task.save()
    return redirect("/tasks/0")


def edittemp(request, id):
    edtask = Task.objects.get(id=id)
    return render(request, "Task/edit.html", {"task": edtask})


def edit(request, id):
    edtask = Task.objects.get(id=id)
    edtask.taskTitle = request.POST["title"]
    edtask.taskPriority = request.POST["prio"]
    edtask.dueDate = request.POST["date"]
    edtask.taskDescription = request.POST["desc"]
    edtask.save()
    return redirect("/tasks/0")


def deleteT(request, id):
    delTask = Task.objects.get(id=id)
    delTask.delete()
    return redirect("/tasks/0")


def today(request, sort=0):
    todayTasks = Task.objects.filter(user=request.user.id, dueDate__date=date.today())
    if sort == 0:
        todayTasks = todayTasks.objects.order_by("taskPriority", "dueDate")
    if sort == 5:
        todayTasks = todayTasks.objects.order_by("-taskPriority", "dueDate")
    if sort == 1:
        todayTasks = todayTasks.objects.order_by("dueDate")
    if sort == 2:
        todayTasks = todayTasks.objects.order_by("-dueDate")
    if sort == 3:
        todayTasks = todayTasks.objects.order_by("taskTitle")
    if sort == 4:
        todayTasks = todayTasks.objects.order_by("-taskTitle")

    return render(request, "Task/today.html", {"tasks": todayTasks})
