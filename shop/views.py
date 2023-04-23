from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "shop/product-list.html"
    context_object_name = 'products'
