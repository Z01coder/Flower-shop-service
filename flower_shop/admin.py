from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Order, OrderItem, CustomUser, Review, Report


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Административная панель для кастомного пользователя."""
    list_display = ('username', 'email', 'phone', 'address', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'address')}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Административная панель для товаров."""
    list_display = ('name', 'price', 'image')
    list_filter = ('price',)
    search_fields = ('name', 'description')
    ordering = ('name',)


class OrderItemInline(admin.TabularInline):
    """Инлайн для товаров заказа."""
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Административная панель для заказов."""
    list_display = ('id', 'user', 'status', 'order_date', 'delivery_date', 'address')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'address')
    list_editable = ('status',)
    ordering = ('-order_date',)
    date_hierarchy = 'order_date'
    inlines = [OrderItemInline]
    readonly_fields = ('order_date',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Административная панель для позиций заказа."""
    list_display = ('id', 'order', 'product', 'quantity')
    list_filter = ('order__status',)
    search_fields = ('order__id', 'product__name')
    ordering = ('-order__order_date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Административная панель для отзывов."""
    list_display = ('user', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'product__name', 'comment')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """Административная панель для отчётов."""
    list_display = ('date', 'total_orders', 'completed_orders', 'revenue', 'expenses')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)