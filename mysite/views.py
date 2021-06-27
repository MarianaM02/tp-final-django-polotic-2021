from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.models import User

from .forms import RegisterForm

def index(request):
    return render(request, 'index.html',{
        #context (un diccionario, dinamicidad)
        'title':'🌘 Killari - Inicio',
        'message': 'Listado de productos',
        'products':[
            # {'title', 'price', 'stock'}
            {'title': 'Playera', 'price': 120, 'stock':True},
            {'title': 'Pantalón', 'price': 120, 'stock':True},
            {'title': 'Camisa', 'price': 120, 'stock':False},
        ]
    })

def login_view(request):
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
       'title':'🌘 Killari - Login',
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
    
    return render(request, 'users/register.html', {
        'title':'🌘 Killari - Registro',
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