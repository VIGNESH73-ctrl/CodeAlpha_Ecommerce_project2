from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem


# 🏠 Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# 🔍 Product Details Page
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


# ➕ Add to Cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('home')


# ❌ Remove from Cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    return redirect('view_cart')


# 🛒 View Cart Page
def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'products': products})


# 📝 User Registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists.")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')


# 🔐 User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login")
    return render(request, 'login.html')


# 🚪 Logout
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


# ✅ Place Order
@login_required
def place_order(request):
    cart = request.session.get('cart', [])
    if not cart:
        return HttpResponse("Your cart is empty")

    order = Order.objects.create(user=request.user)

    for pid in cart:
        product = Product.objects.get(id=pid)
        OrderItem.objects.create(order=order, product=product)

    request.session['cart'] = []  # Empty cart after placing order
    return render(request, 'order_success.html', {'order': order})
