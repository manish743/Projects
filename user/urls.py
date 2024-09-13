from django.urls import path
from user import views as user_view
from django.contrib.auth import views as auth
from . import views
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', Login, name="login"),
    path('logout/', auth.LogoutView.as_view(template_name="user/index.html"), name="logout"),
    path('register/', register, name="register"),
    path('', views.index, name="index"),
]