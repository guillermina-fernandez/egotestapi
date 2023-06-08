from django.urls import path
from . import views
from .endpoints import *


urlpatterns = [
    path('productos/', views.ProductsView.as_view(), name='productos'),
    path('get_products/', get_products),
    path('get_product/<int:pk>/', get_product),
    path('post_product/', post_product),
    path('put_product/<int:pk>/', put_product),
    path('delete_product/<int:pk>/', delete_product),
]
