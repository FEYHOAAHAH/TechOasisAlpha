from django import forms
from userapp.models import *


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'average_score', 'review_description']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'average_score', 'review_description']