from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('categories/', category_list, name="categories"),
    path('questions/', question_list, name='question_list'),
    path('question/<int:question_id>/answers/', answer_list, name='answer_list'),
]
