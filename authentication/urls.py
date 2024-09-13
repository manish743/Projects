from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
]