from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("", product_list, name="product_list"),
    path("product/<int:pk>/<str:name>/", product_detail, name="product_detail"),
]