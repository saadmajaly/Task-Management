from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request,sort):
    if(sort==0):
        tasks=Task.objects.all().order_by('taskPriority','dueDate')
    if(sort==5):
        tasks=Task.objects.all().order_by('-taskPriority','dueDate')
    if(sort==1):
        tasks=Task.objects.all().order_by('dueDate')
    if(sort==2):
        tasks=Task.objects.all().order_by('-dueDate')
    if(sort==3):
        tasks=Task.objects.all().order_by('taskTitle')
    if(sort==4):
        tasks=Task.objects.all().order_by('-taskTitle')
    return render(request,"Task/index.html",{"tasks":tasks})
def addtemp(request):
    
    return render(request,"Task/add.html")
@csrf_exempt

def add(request):
    title=request.POST["title"]
    date=request.POST["date"]
    description=request.POST["desc"]
    priority=request.POST["prio"]
    task = Task(taskTitle=title,dueDate=date,taskDescription=description,taskPriority=priority)
    task.save()
    return redirect("/0")

def edittemp(request,id):
    edtask=Task.objects.get(id=id)
    return render(request,"Task/edit.html",{'task':edtask})

def edit(request,id):
    edtask=Task.objects.get(id=id)
    edtask.taskTitle=request.POST["title"]
    edtask.dueDate=request.POST["date"]
    edtask.taskDescription=request.POST["desc"]
    edtask.save()
    return redirect("/0")

def deleteT(request,id):
    delTask=Task.objects.get(id=id)
    delTask.delete()
    return redirect("/0")