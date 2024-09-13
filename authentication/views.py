from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, template_name="authentication/home.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username.")
            return redirect('/authentication/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect('/authentication/login/')
        else:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('/authentication/home/')
    
    return render(request, template_name="authentication/login.html")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/authentication/register/')
        
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully!")
        return redirect('/authentication/home/')
    
    return render(request, template_name="authentication/register.html")