from django.shortcuts import  render, redirect
from .forms import UserForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'testapp/base.html', {})


@login_required(login_url='/user_login')
def user_logout(request):
    logout(request)
    return render(request, 'testapp/login.html', {})


def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			return render(request, 'testapp/login.html', {})
		else:
			return HttpResponse("something went wrong")
	else:
		user_form = UserForm()
		return render(request,'testapp/registration.html',
                          {'user_form':user_form,
                           'registered':registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'testapp/base.html', {})
			else:
				return HttpResponse("Your account was inactive.")
		else:
			print("Someone tried to login and failed.")
			print("They used username: {} and password: {}".format(username,password))
			return HttpResponse("Invalid login details given")
	else:
		return render(request, 'testapp/login.html', {})


@login_required(login_url='/user_login')
def product(request):
	if request.method == 'POST':
		product_form = ProductForm(request.POST, request.FILES)
		if product_form.is_valid():
			product_form.save()
			return redirect("/get_products")
		else:
			return HttpResponse(str(product_form.errors))
	else:
		product_form = ProductForm()

		return render(request,'testapp/product.html',
                          {'product_form':product_form})


@login_required(login_url='/user_login')
def get_product(request):
	if request.method == 'GET':
		product_list = Product.objects.filter(owner=request.user)
		return render(request, 'testapp/get_prod.html', {'prod': product_list})


@login_required(login_url='/user_login')
def update_product(request, id): 
	obj = get_object_or_404(Product, id = id)

	form = ProductForm(request.POST or None, instance = obj)

	if form.is_valid(): 
		form.save() 
		return redirect("/get_products")
	return render(request, "testapp/product.html", {'product_form':form})

@login_required(login_url='/user_login')
def destroy(request, id):  
	obj = get_object_or_404(Product, id = id)
	obj.delete()
	return redirect("/get_products")
