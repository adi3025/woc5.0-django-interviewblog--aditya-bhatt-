from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout




        
          
def register(request):
     submitted = False
     
     if request.method == "POST":
          form = StudentForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/register?submitted = True')
     else:
          form = StudentForm
          if 'submitted' in request.GET:
               submitted = True                       
     
     return render(request,'app1/register.html',{'form':form,'submitted':submitted})
def admin(request):
     return render(request,'app1/admin.html')
def PostLogin(request):
     return render(request,'app1/PostLogin.html')
