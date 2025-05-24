from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm


def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def cars_view(request):
    products = Product.objects.all()
    return render(request, 'cars.html', {'products': products})


def about_view(request):
    return render(request, 'about.html')


def accessories_view(request):
    return render(request, 'accessories.html')


def contacts_view(request):
    return render(request, 'contacts.html')


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})


def order_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return render(request, 'order_success.html', {'product': product, 'order': order})
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form, 'product': product})
