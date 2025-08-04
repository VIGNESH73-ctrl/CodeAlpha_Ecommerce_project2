from django.db import models
from django.contrib.auth.models import User

# 🛍️ Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name

# 📦 Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

# 🧾 Order Item Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}"

