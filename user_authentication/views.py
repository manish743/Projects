from django.shortcuts import render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
# Class based view for login
class CustomLoginView(LoginView):
    template_name = 'user_authentication/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True  # Redirects already authenticated users
    success_url = reverse_lazy('home')  # Redirect after successful login


# Function based view for Login
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm

# def custom_login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, template_name="auth/login.html", context={'form' : form})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')    # Redirect to home page after logout

# def custom_logout_view(request):
#     logout(request)
#     return redirect('home')


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, template_name="user_authentication/register.html", context={'form' : form})


def home_view(request):
    return HttpResponse("Welcome!!")