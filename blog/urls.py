from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_list, name="blog_list"),
    path('<int:pk>/', blog_detail, name="blog_detail"),
    path('<int:pk>/edit/', edit_blog, name="edit_blog"),
    path('<int:pk>/delete/', delete_blog, name="delete_blog"),
]