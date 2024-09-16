from django.urls import path

from .views import create_product, index, get_products

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('list/', get_products, name='get_products'),
    path('', index, name='index')
]
