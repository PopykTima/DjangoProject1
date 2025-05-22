from django.shortcuts import render, get_object_or_404
from .models import Product

def home_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'home.html', context)

def models_view(request):
    return render(request, 'models.html')

def parts_view(request):
    return render(request, 'parts_page.html')

def service_view(request):
    return render(request, 'service_page.html')

def contact_view(request):
    return render(request, 'contact_information_page.html')

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
