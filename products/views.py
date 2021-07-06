from django.shortcuts import render

from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product
from .forms import NewProductForm

# Create your views here.
class ProductListView(ListView):
  template_name = 'index.html'
  queryset = Product.objects.all().order_by('-id')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context ['products']=context['product_list']

    return context

class ProductDetailView(DetailView):
  #busqueda por id
  model = Product
  template_name = 'products/product.html'

class ProductSearchListView(ListView):
  template_name = 'products/search.html'

  def get_queryset(self):
    filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
    return Product.objects.all().filter(filters)

  def query(self):
    return self.request.GET.get('q')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['query'] = self.query()
    context['count'] = context['product_list'].count()
    return context

def new(request):
  context = {}
  
  if not request.user.is_superuser:
    return redirect('index')

  form = NewProductForm(request.POST, request.FILES)

  if request.method == 'POST' and form.is_valid():
    title = form.data.get('title')
    description = form.data.get('description')
    price = form.data.get('price')
    product = Product(title=title, image=request.FILES['image'], thumbnail=request.FILES['thumbnail'], description=description, price=price)
    product = form.save()
    
    if product:
      messages.success(request, 'Producto creado exitosamente')
      return redirect('index')
  
  context['form'] = form

  return render(request, 'products/new.html', context)