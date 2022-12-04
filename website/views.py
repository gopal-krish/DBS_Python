from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponse

def home(request):a
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'website/home.html',conext)
