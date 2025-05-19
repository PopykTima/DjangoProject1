# DjangoProject1/views.py

from django.shortcuts import render

def home_view(request):
    """Головна сторінка проекту."""
    return render(request, 'home.html')

def about_view(request):
    """Сторінка 'Про нас'."""
    return render(request, 'about.html')

def contact_view(request):
    """Контактна сторінка."""
    return render(request, 'contact.html')