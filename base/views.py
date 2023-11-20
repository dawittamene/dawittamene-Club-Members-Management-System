from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm



def index(request):
    return render(request, 'base/index.html')
       
   



def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request, "username or password is incorrect")
    context ={}
    return render(request, 'base/login.html', context)


def signuppage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account created successfully for ' + user)
            return redirect('loginpage')
        
    context ={'form':form}
    return render(request, 'base/signup.html', context)
def logoutPage(request):
    logout(request)
    return redirect('loginpage')




    
          



    

