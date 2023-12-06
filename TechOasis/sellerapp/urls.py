from django.urls import path
from sellerapp.views import *


urlpatterns  = [
    path('adminhome/', AdminProductsView.as_view(), name='adproducts'),
    path('create/', ProductCreateView.as_view(), name='createp'),
    path('<pk>/update/', ProductUpdateView.as_view(), name='updatep'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='deletep')
]