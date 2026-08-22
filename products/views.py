from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def productList(requette):
    products =Product.objects.all()
    for product in products:
       reponse=f"{product.name}:{product.price}"
    return HttpResponse(reponse)
