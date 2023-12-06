from django.urls import path
from userapp.views import *


urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name="product_detail")
]