from django.contrib import admin


# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  fields = ('title', 'description', 'price', 'image', 'thumbnail')
  list_display = ('__str__', 'slug')

admin.site.register(Product, ProductAdmin)