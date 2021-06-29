from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

# Create your views here.
class ProductListView(ListView):
  template_name = 'index.html'
  queryset = Product.objects.all().order_by('-id')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context ['message']='Galería'
    context ['products']=context['product_list']

    return context

class ProductDetailView(DetailView):#busqueda por id
  model = Product
  template_name = 'products/product.html'