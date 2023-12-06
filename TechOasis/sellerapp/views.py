from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .forms import *

from userapp.models import *

# Create your views here.



class AdminProductsView(ListView):
    model = Product
    template_name = 'sellerapp/product_admin_list.html'
    context_object_name = 'adproducts'



class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'sellerapp/create_product.html'
    success_url = '/adminhome/'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'sellerapp/update_product.html'
    success_url = '/adminhome/'



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'sellerapp/delete_product.html'
    success_url = '/adminhome/'




