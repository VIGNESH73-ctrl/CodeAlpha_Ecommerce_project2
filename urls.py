"""
URL configuration for Ecommerce_project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views  # Import all views from store app

urlpatterns = [
    # 🔧 Admin Panel
    path('admin/', admin.site.urls),

    # 🏠 Home Page
    path('', views.home, name='home'),

    # 🛒 Cart System
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),

    # 🔐 Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 📦 Order Processing
    path('place-order/', views.place_order, name='place_order'),

    # 🔍 Product Detail Page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
