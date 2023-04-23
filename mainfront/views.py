from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from products.models import Product

# Create your views here.
class HomepageView(ListView):
   template_name = 'mainfront/home-page.html'
   queryset = Product.objects.all()
   context_object_name = 'products'


class AboutPageView(TemplateView):
   template_name = 'mainfront/about-page.html'


class ContactPageView(TemplateView):
   template_name = 'mainfront/contact-page.html'