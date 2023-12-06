from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'userapp/product_list_view.html'
    context_object_name = 'products'



class ProductDetailView(DetailView):
    model = Product
    template_name = 'userapp/product_detail_view.html'
    context_object_name = 'products'



