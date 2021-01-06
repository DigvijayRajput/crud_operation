from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from testapp.models import Product


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email', 'password',)


class ProductForm(forms.ModelForm):
	
	class Meta():
		model = Product
		fields = '__all__'
