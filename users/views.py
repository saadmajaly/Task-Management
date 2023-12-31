from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as loguser
from django.contrib.auth import logout as logouser

# Create your views here.
def login(request,ermsg=""):
 if(len(ermsg)>0):
   return render(request, 'login.html',{'loginerror':'Invalid login credentials'})
 return render(request, 'login.html')          

def auth(request):
 usern=request.POST.get("username")
 passw=request.POST.get("password")
 
 user=authenticate(request,username=usern,password=passw)
 if user is not None:
  loguser(request,user)
  return redirect("/tasks/")
 else:
  return redirect("/erlog/ermsg='the login credentials are wrong'")

def userNameUni(username):
 try:
  User.objects.get(username=username)
  return False
 except User.DoesNotExist:
  return True
 
def emailUni(email):
 try:
  User.objects.get(email=email)
  return False
 except User.DoesNotExist:
  return True

def signup(request):
 
 return render(request, 'signup.html')

def create(request):
 usern=request.POST["username"]
 email=request.POST["email"]
 passw=request.POST["password"]
 passconf=request.POST["password_confirmation"]
 if(userNameUni(usern) & emailUni(email)):
  nuser=User.objects.create_user(usern,email,passw)
  nuser.save()
  return redirect('/')
 elif(userNameUni(usern)):
  errormsg="Email address already exists."
  return render(request,"signup.html",{'ermsg':errormsg,'email':email,'usern':usern,'pass':passw,'passc':passconf})
 elif(emailUni):
  errormsg="email already exists."
  return render(request,"signup.html",{'ermsg':errormsg,'email':email,'usern':usern,'pass':passw,'passc':passconf})

def lgoout(request):
  logouser(request)
  return redirect(reverse('login'))