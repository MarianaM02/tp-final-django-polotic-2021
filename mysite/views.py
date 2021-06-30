from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

#from django.contrib.auth.models import User
from users.models import User

from products.models import Product

from .forms import RegisterForm



def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'index.html',{
        #context (un diccionario, dinamicidad)
        'title':'Killari - Inicio',
        'message': 'Listado de productos',
        'products': products,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username = request.POST.get('username') 
        #es un diccionario, utilizamos metodo get
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}!'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')


    return render(request, 'users/login.html',{
       'title':'Killari - Login',
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
    
    return render(request, 'users/register.html', {
        'title':'Killari - Registro',
        'form': form,
    })

def about(request):
    return render(request, 'about.html', {
        'title':'🌘 Killari - Sobre Nosotras',
    
    })

def search(request):
    return render(request, 'search.html', {
        'title':'🌘 Killari - Resultado de la Búsqueda',
    
    })

def item(request):
    return render(request, 'item.html', {
        'title':'🌘 Killari - Producto',
    
    })