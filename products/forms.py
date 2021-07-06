from django import forms
#from django.contrib.auth.models import User
# from users.models import User
from .models import Product

class NewProductForm(forms.ModelForm):
  class Meta:
        model = Product
        fields = "__all__"
        exclude = ['slug']