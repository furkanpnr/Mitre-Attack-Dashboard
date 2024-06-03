from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.

def login_request(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        context = {"active_form": "Login"}
        
        if user is None:
            context['login_error'] = "Invalid username or password"
            context['username1'] = username
            return render(request, 'account/login-register.html', context=context)

        login(request, user)
        return redirect('home')
    
    return render(request, 'account/login-register.html', {"active_form": "Login"})

def register_request(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context = {"active_form": "Register"}
        
        if User.objects.filter(username=username).exists():
            context['register_error'] = "Username already exist!"
        if User.objects.filter(email=email).exists():
            context['register_error'] = "Email already exist!"
        
        if context.get('register_error', None):
            context['username2'] = username
            context['email'] = email
            return render(request, 'account/login-register.html', context=context)
        
        user = User.objects.create(username=username, email=email, password=password)
        
        return redirect('login')
        
    return render(request, 'account/login-register.html', {"active_form": "Register"})

def logout_request(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    logout(request)
    return redirect('login')