from django.shortcuts import render
from .models import product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    dict_01 = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/index2.html', dict_01)



def about(request):
    return render(request, 'shop/about.html')
    # return HttpResponse("hello a")

def contact(request):
    return HttpResponse('hello c')

def status(request):
    return HttpResponse('hello t')

def search(request):
    return HttpResponse('hello s')

def products(request):
    return HttpResponse('hello p')

def checkout(request):
    return HttpResponse('hello co ')

def karts(request):
    return HttpResponse('hello k')
