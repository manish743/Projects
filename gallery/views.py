from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, template_name="gallery/product_list.html", context={'products' : products})

