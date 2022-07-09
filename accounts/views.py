from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['Password']


        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'user doesnot exist')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
       firstname=request.POST['firstname']
       lastname=request.POST['lastname']
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       confirmPassword=request.POST['confirm_password']

       if password==confirmPassword:
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error('request','email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                messages.success(request,'you are registered')
                auth.login(request,user)
                messages.success(request,'you are now loged in')
                return redirect('dashboard')
                # user.save()
                # messages.success(request,'you are registered')
                # return redirect('login')
       else:
        messages.error(request,'password doesnot match')
        return render(request,'accounts/register.html')

    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        # messages.success(request,'you are successfully logged out')
        return redirect('home')
    return redirect('home')
