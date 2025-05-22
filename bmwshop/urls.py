from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('models/', views.models_view, name='models'),
    path('parts/', views.parts_view, name='parts'),
    path('service/', views.service_view, name='service'),
    path('contact/', views.contact_view, name='contact'),

    # Шлях до сторінки деталей продукту
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
]
