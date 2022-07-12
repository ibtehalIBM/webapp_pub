from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Product, User
from .forms import UserForm
from django.forms import modelform_factory

# Create your views here.

def home(request):
    return render(request, 'main_app/Home.html')

def products(request):
    return render(request, "main_app/products.html",
                  {"products": Product.objects.all()})

def users(request):
    return render(request, "main_app/Users.html",
                  {"users": User.objects.all()})

def productsByID(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request, 'main_app/Product.html',{"product": product})


def register(request):
    form = UserForm()
    if request.method=="POST":
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_app/Home.html")
    return render(request,"main_app/NewUser.html",{"form":form})
