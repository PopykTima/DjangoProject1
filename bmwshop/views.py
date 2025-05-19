from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Головна сторінка</h1><a href='/models/'>Моделі</a> | <a href='/parts/'>Запчастини</a> | <a href='/service/'>Сервіс</a> | <a href='/contact/'>Контакти</a>")

def models_view(request):
    return HttpResponse("<h1>Моделі BMW</h1><a href='/'>На головну</a>")

def parts_view(request):
    return HttpResponse("<h1>Запчастини</h1><a href='/'>На головну</a>")

def service_view(request):
    return HttpResponse("<h1>Сервіс</h1><a href='/'>На головну</a>")

def contact_view(request):
    return HttpResponse("<h1>Контакти</h1><a href='/'>На головну</a>")