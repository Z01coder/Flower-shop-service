from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileEditForm
from .forms import ReviewForm
from .models import Product, Review, Order, OrderItem, Report
from .forms import OrderForm
from datetime import date
import logging

logger = logging.getLogger(__name__)


def home(request):
    """Главная страница сайта."""
    return render(request, 'home.html')

def register(request):
    """Регистрация нового пользователя."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_profile(request):
    """Редактирование профиля пользователя."""
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

def product_list(request):
    """Список всех товаров."""
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


def product_detail(request, product_id):
    """Детальная страница товара с отзывами."""
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
    })

def add_to_cart(request, product_id):
    """Добавление товара в корзину."""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')


def view_cart(request):
    """Просмотр содержимого корзины."""
    cart = request.session.get('cart', {})
    products = []
    total_price = 0
    cart_to_update = {}
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            products.append({
                'product': product,
                'quantity': quantity,
                'total': product.price * quantity
            })
            total_price += product.price * quantity
            cart_to_update[product_id] = quantity
        except Product.DoesNotExist:
            # Товар был удален из БД, пропускаем его
            continue
    # Обновляем корзину, удаляя несуществующие товары
    request.session['cart'] = cart_to_update
    return render(request, 'catalog/cart.html', {'products': products, 'total_price': total_price})


def clear_cart(request):
    """Очистка корзины."""
    # Удаляем корзину из сессии
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('product_list')

@login_required
def create_order(request):
    """Создание нового заказа из корзины."""
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Корзина пуста. Добавьте товары перед оформлением заказа.")
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for product_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=int(product_id))
                    OrderItem.objects.create(order=order, product=product, quantity=quantity)
                except Product.DoesNotExist:
                    continue

            # Финализация заказа
            order.is_finalized = True
            order.save()

            request.session['cart'] = {}
            return redirect('order_history')
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form})


@login_required
def order_history(request):
    """История заказов пользователя."""
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def repeat_order(request, order_id):
    """Повторение ранее сделанного заказа."""
    old_order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Создаем OrderItem для каждого товара из старого заказа
    order_items_data = []
    for item in old_order.orderitem_set.all():
        order_items_data.append({
            'product': item.product,
            'quantity': item.quantity
        })
    
    # Создаем заказ сразу с is_finalized=True, чтобы избежать двойного сигнала
    new_order = Order.objects.create(
        user=request.user,
        delivery_date=old_order.delivery_date,
        delivery_time=old_order.delivery_time,
        address=old_order.address,
        comment=old_order.comment,
        status='pending',
        is_finalized=True
    )

    # Создаем OrderItem для каждого товара
    for item_data in order_items_data:
        OrderItem.objects.create(
            order=new_order,
            product=item_data['product'],
            quantity=item_data['quantity']
        )

    messages.success(request, "Заказ успешно повторен!")
    return redirect('order_history')

@login_required
def profile(request):
    """Личный кабинет пользователя."""
    return render(request, 'registration/profile.html')


@login_required
def analytics(request):
    """Аналитика по продажам (только для суперпользователей)."""
    if not request.user.is_superuser:
        return redirect('home')

    # Генерация данных для отчётов
    today = date.today()

    # Получение выполненных заказов
    total_orders = Order.objects.count()  # Всего заказов
    completed_orders = Order.objects.filter(status='completed').count()  # Выполненные заказы

    # Расчёт выручки (с учетом количества товаров)
    revenue = OrderItem.objects.filter(
        order__status='completed'
    ).aggregate(
        total_revenue=Sum(F('quantity') * F('product__price'))
    )['total_revenue'] or 0

    # Расходы (фиксированные)
    expenses = 5000  # Пример: фиксированные расходы

    # Создание или обновление отчёта
    report, created = Report.objects.get_or_create(date=today, defaults={
        'total_orders': total_orders,
        'completed_orders': completed_orders,
        'revenue': revenue,
        'expenses': expenses,
    })

    # Передача всех отчётов в шаблон
    reports = Report.objects.all()
    return render(request, 'analytics/analytics.html', {'reports': reports})