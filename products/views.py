from django.shortcuts import render
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from products.forms import ProductForm
from django.shortcuts import render, redirect, reverse

from products.models import Product

# Create your views here.
class ProductDetailView(DetailView):
   template_name = 'products/product-detail.html'
   context_object_name = "product"

   def get_success_url(self):
        return reverse("main:home-page")


class ProductCreateView(CreateView):
   template_name = 'products/product-create.html'
   form_class = ProductForm

   def get_success_url(self):
        return reverse("main:home-page")


class ProductUpdateView(UpdateView):
   queryset = Product.objects.all()
   template_name = 'products/product-update.html'
   form_class = ProductForm

   def get_success_url(self):
        return reverse("main:home-page")


class ProductDeleteView(DeleteView):
   queryset = Product.objects.all()
   template_name = 'products/product-delete.html'

   def get_success_url(self):
        return reverse("main:home-page")