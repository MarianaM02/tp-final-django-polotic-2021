from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html',{
        #context (un diccionario, dinamicidad)
        'title':'Productos',
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
       'title':'Login',
    })