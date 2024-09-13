from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    return HttpResponse("<h1> Hello world! </h1>")

def product_list(request):
    products = Product.objects.all()
    return render(request, template_name="ecommerce_catalog/index.html", context={'products' : products})

def product_detail(request, pk, name):
    product = Product.objects.get(pk = pk)
    return render(request, template_name="ecommerce_catalog/product_detail.html", context={'product' : product})