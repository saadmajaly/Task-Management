from django.shortcuts import render,redirect
from django.urls import reverse
from .models import User
# Create your views here.
def signin(request):
 
 return render(request, 'signin.html')

def signup(request):
 
 return render(request, 'signup.html')

def create(request):
 usern=request.POST["username"]
 email=request.POST["email"]
 passw=request.POST["password"]
 nuser=User(username=usern,email=email,password=passw)
 nuser.save()
 return redirect(reverse('signin'))