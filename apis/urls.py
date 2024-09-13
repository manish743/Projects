from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('todos/', todo_list, name="todo_list"),
    path('todos/<int:pk>/', todo_detail, name="todo_detail"),
]