from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
PRODUCTS = [
{"id": 1, "name": "Laptop", "price": 1800},
{"id": 2, "name": "Headphones", "price": 150},
{"id": 3, "name": "Mouse", "price": 40},
]

def home(request):
    return HttpResponse("<h1>myshop</h1><br><a href='/products/'>პროდუქტების ნახვა</a> | <a href='/about/'>ჩვენ შესახებ</a>")

def about(request):
    return HttpResponse("<h1>ჩვენ შესახებ</h1> <p>ეს არის ჩვენი სასწავლო ონლაინ მაღაზია myshop.</p><br><a href='/'>მთავარი გვერდი</a>")

def product_list(request):
    html = "<h1>პროდუქტების სია</h1><ul>"
    for product in PRODUCTS:
        html += f"<li><a href='/products/{product['id']}/'>{product['name']}</a> — ფასი: {product['price']} ლარი</li>"
        html += "</ul><br><a href='/'>მთავარი გვერდი</a>"
    return HttpResponse(html)

def products_detail(request, pk):
    product = None 
    for p in PRODUCTS:
        if p["id"] == pk:
            product = p
            break

    if product:
        html = f"<h1>{product['name']}</h1><p>ფასი: {product['price']} ლარი</p>"
    else:
        raise Http404("პროდუქტი ვერ მოიძებნა")
    
    html += "<br><a href='/products/'>უკან პროდუქტებში</a>"
    return HttpResponse(html)