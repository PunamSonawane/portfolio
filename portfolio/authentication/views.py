from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def authlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'Invalid Username or Password')

    return render(request,'authentication/login.html')

def forgetpassword(request):
    return render(request,'authentication/forget.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.error(request,'Username already exist')
            elif User.objects.filter(email=email):
                messages.error(request,'Email already exist')
            else:
                user=User.objects.create_user(username=name,password=password,email=email)
                user.save()
                return redirect('profile')
        else:
            messages.error(request,'Passwords not matched')


    return render(request,'authentication/register.html')

def authlogout(request):
    logout(request)
    messages.success(request,'Logout Successfully !')
    return redirect('login')
