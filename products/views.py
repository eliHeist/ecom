from django.views.generic import UpdateView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from products.forms import ProductForm
from django.shortcuts import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
class ProductDetailView(DetailView):
   model = Product
   template_name = 'products/product-detail.html'
   context_object_name = "product"


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


class ProductSearchView(TemplateView):
    template_name = "products/search.html"



@api_view(["GET"])
def productApiView(request):
   # get all products from db
   products = Product.objects.all()
   # create empty list of products to send back
   allProducts = []
   # loop through the products
   for product in products:
      # create a dictionary from each product
      product_dictionary = {
         'pk': product.pk,
         'name': product.name,
         'picture': product.picture.url,
         'actualPrice': product.actualPrice(),
         'price': product.formatedPrice(),
         'description': product.description,
         'cartegories': [cartegory.name for cartegory in product.cartegories.all()],
         'discount': product.discount
      }
      # append the dictionary to the product list
      allProducts.append(product_dictionary)
   print(allProducts)
   serializer = ProductSerializer(products, many=True)
   
   return Response(allProducts)