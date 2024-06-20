from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


#  GET /products
def index(req):
    products = Product.objects.all()
    return render(req, 'index.html', {'products': products})


def new(req):
    return HttpResponse('New Product')


