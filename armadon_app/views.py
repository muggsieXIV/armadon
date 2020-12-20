from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    return redirect('/amadon')

def amadon(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'amadon.html', context)

def process_product(request):
    product = Product.objects.get(id='product_id')
    return redirect('/armadon/<int:product_id>/checkout')

def checkout(request): 
    return render(request, 'checkout.html')

