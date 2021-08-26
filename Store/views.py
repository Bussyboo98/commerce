from django.shortcuts import get_object_or_404, render

from Store.models import *

# Create your views here.




def product_all(request):
    products = Products.products.all()
    return render(request, 'Store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug, in_stock=True)
    return render(request, 'Store/products/single.html', {'product':product})
 
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Products.objects.filter(category=category)
    return render (request, 'Store/products/category.html', {'category' : category, 'products' : products})
