from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cars/', views.cars_view, name='cars'),
    path('about/', views.about_view, name='about'),
    path('accessories/', views.accessories_view, name='accessories'),
    path('contact/', views.contacts_view, name='contact'),  # ✅ виправлено тут

    # Детальна сторінка товару
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),

    # Форма оформлення замовлення
    path('product/<slug:slug>/order/', views.order_view, name='order_product'),
]
