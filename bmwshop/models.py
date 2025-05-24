from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    slug = models.SlugField(unique=True, blank=True, help_text="Унікальний URL-ідентифікатор категорії")
    description = models.TextField(blank=True, verbose_name="Опис категорії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'В наявності'),
        ('out_of_stock', 'Немає в наявності'),
        ('coming_soon', 'Очікується'),
    ]

    CONDITION_CHOICES = [
        ('new', 'Новий'),
        ('used', 'Вживаний'),
        ('refurbished', 'Відновлений'),
    ]

    name = models.CharField(max_length=200, verbose_name="Назва товару")
    slug = models.SlugField(unique=True, blank=True, help_text="Унікальний URL-ідентифікатор товару")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категорія")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Артикул")
    description = models.TextField(verbose_name="Опис товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Ціна")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                         verbose_name="Ціна зі знижкою")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Статус")
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new', verbose_name="Стан товару")
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1916),
            MaxValueValidator(2025)
        ],
        verbose_name="Рік випуску",
        help_text="Рік випуску моделі BMW"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендований товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість в наявності")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Зображення товару")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата додавання")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_discount_percentage(self):
        if self.discount_price and self.price:
            return int(100 - (self.discount_price * 100 / self.price))
        return 0

    class Meta:
        verbose_name = "Товар BMW"
        verbose_name_plural = "Товари BMW"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


# НОВА МОДЕЛЬ ЗАМОВЛЕННЯ
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    full_name = models.CharField(max_length=100, verbose_name="ПІБ")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адреса доставки")
    comment = models.TextField(blank=True, null=True, verbose_name="Коментар до замовлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ['-created_at']

    def __str__(self):
        return f"Замовлення {self.full_name} - {self.product.name}"
