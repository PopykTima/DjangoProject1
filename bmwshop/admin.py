# bmwshop/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    date_hierarchy = 'created_at'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount_price', 'status', 'quantity', 'is_featured', 'created_at']
    list_filter = ['status', 'condition', 'category', 'is_featured', 'created_at']
    search_fields = ['name', 'description', 'sku']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'discount_price', 'status', 'is_featured']
    date_hierarchy = 'created_at'
    raw_id_fields = ['category']
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'slug', 'category', 'sku', 'description')
        }),
        ('Цінова політика', {
            'fields': ('price', 'discount_price')
        }),
        ('Статус та наявність', {
            'fields': ('status', 'condition', 'quantity', 'year')
        }),
        ('Медіа та промо', {
            'fields': ('image', 'is_featured')
        }),
        ('Дати', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )