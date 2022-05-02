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
    # dict_01 = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # return render(request, 'shop/index.html', dict_01)

    allProds =[[products, range(1, len(products)), nSlides],
               [products, range(1, len(products)), nSlides]]
    dict_02 = {'allProds': allProds }
    return render(request, "shop/index.html", dict_02)




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
