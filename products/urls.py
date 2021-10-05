from django.urls import path
from .views import product_detail_view, Product_create_view

urlpatterns = [
    path('products/', product_detail_view, name='view-products'),
    path('create/', Product_create_view, name='create-product'),
]
