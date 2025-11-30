from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Кастомная модель пользователя с дополнительными полями."""
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

class Product(models.Model):
    """Модель товара (букета цветов)."""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Order(models.Model):
    """Модель заказа на доставку цветов."""
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('processing', 'В работе'),
        ('shipped', 'Отправлен'),
        ('completed', 'Выполнен'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    is_finalized = models.BooleanField(default=False)
    is_repeated = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-order_date',)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    """Модель позиции заказа (связь заказа с товаром и количеством)."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
        ordering = ('order', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"

class Review(models.Model):
    """Модель отзыва на товар."""
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created_at',)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"

class Report(models.Model):
    """Модель отчёта по продажам за день."""
    date = models.DateField()
    total_orders = models.IntegerField()
    completed_orders = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ('-date',)
        unique_together = ('date',)

    def __str__(self):
        return f"Report for {self.date}"