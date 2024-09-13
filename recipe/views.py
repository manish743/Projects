from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse

# Create your views here.
def recipes(request):
    if request.method == "POST":
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        Recipe.objects.create(recipe_name = recipe_name, recipe_description = recipe_description,
                              recipe_image = recipe_image)
        # return HttpResponse("Recipe submitted successfully")
        return redirect('/recipe')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name__icontains = request.GET.get('search')
        )

    context = {'recipes' : queryset}
    return render(request, template_name="recipe/recipes.html", context = context)
    
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image
        
        queryset.save()
        return redirect('/recipe')
    
    return render(request, template_name="recipe/update_recipe.html", context={'recipe' : queryset})