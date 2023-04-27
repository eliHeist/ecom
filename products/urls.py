from django.urls import path

from products.views import ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView, productApiView, ProductSearchView

app_name = 'products'

urlpatterns = [
   path('create/', ProductCreateView.as_view(), name='product-create'),
   path('search/', ProductSearchView.as_view(), name='product-search'),
   path('api/', productApiView, name='product-api'),
   path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
   path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
   path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]