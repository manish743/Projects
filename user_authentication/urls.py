from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login_auth"),
    path('logout/', CustomLogoutView.as_view(), name="logout_auth"),
    path('register/', register_view, name="register_auth"),
    path('home', home_view, name="home"),
]