from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings 

from . import views

from products.views import ProductListView


urlpatterns = [
	path('', ProductListView.as_view(), name='index'), ##funcion recibe 2 argumentos, direccion vacia va a index
	path('users/login', views.login_view, name='login'),
	path('users/logout', views.logout_view, name='logout'),
	path('users/register', views.register, name='register'),
	path('about', views.about, name='about'),

	path('admin/', admin.site.urls),
	path('products/', include('products.urls')),
	#products/:id
	path('carts/', include('carts.urls')),
	

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)