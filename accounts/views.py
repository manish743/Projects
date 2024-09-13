from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, template_name="accounts/register.html", context={'form' : form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username and password")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = UserLoginForm()
    return render(request, template_name="accounts/login.html", context={'form' : form})

def home_view(request):
    return render(request, template_name="accounts/home.html")