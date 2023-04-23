from django.urls import path

from products.views import ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView

app_name = 'products'

urlpatterns = [
   path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
   path('create/', ProductCreateView.as_view(), name='product-create'),
   path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
   path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]