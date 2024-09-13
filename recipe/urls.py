from django.urls import path
from .views import *

urlpatterns = [
    path("", recipes, name="recipe"),
    path("update_recipe/<id>/", update_recipe, name="update_recipe"),
    path("delete_recipe/<id>/", delete_recipe, name="delete_recipe"),
]