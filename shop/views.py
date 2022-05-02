from django.shortcuts import render
from .models import product, contact, checkout, status
from math import ceil
# import logging
import json
# logger = logging.getLogger(__name__)
from django.http import HttpResponse


def about(request):
    return render(request, 'shop/about.html')


def index(request):
    all_products = []
    categories_of_products = product.objects.values('category', 'id')
    all_categories = {item['category'] for item in categories_of_products}
    for thing in all_categories:
        filtered_products = product.objects.filter(category=thing)
        n = len(filtered_products)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([filtered_products, range(1, nslides), nslides])
    dict_02 = {'all_products': all_products}
    return render(request, "shop/index.html", dict_02)


def products(request, my_id):
    # fetch product using id
    Product = product.objects.filter(id=my_id)
    # print(Product)
    return render(request, 'shop/Products.html', {'product': Product[0]})


def contacts(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact = contact(name=name, email=email, phone=phone, desc=desc)
        Contact.save()
        thank = True
    return render(request, "shop/Contact.html", {'thank': thank})


def checkouts(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        First_name = request.POST.get('First_name', '')
        Last_name = request.POST.get('Last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        Address = request.POST.get('Address', '') + " " + request.POST.get('Address_2', '')
        Country = request.POST.get('Country', '')
        State = request.POST.get('State', '')
        zip_code = request.POST.get('Zip', '')
        Checkout = checkout(items_json=items_json, First_name=First_name, Last_name=Last_name, email=email,
                             phone=phone, Address=Address, Country=Country, State=State, zip_code=zip_code)
        Checkout.save()
        update = status(order_id=Checkout.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = Checkout.order_id
        return render(request, 'shop/Checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/Checkout.html')


def Status(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            Checkout = checkout.objects.filter(order_id=orderId, email=email)
            if len(Checkout) > 0:
                update = status.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, Checkout[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{ }')
        except Exception as e:
            return HttpResponse(f'exception {e}')

    return render(request, 'shop/Status.html')


def Cart(request):
    return render(request, 'shop/Cart.html')

def Payment(request):
    return render(request, 'shop/Payment.html')

