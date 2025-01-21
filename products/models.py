"""
This module defines models for categories, products, and user product likes.
"""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a product category with a name and an optional friendly name
    for display purposes.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the category name.
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the category, if available.
        """
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product with details such as category, SKU, name,
    description, price, rating, and image data.
    """

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the product name.
        """
        return self.name


class Like(models.Model):
    """
    Represents a "like" action by a user on a product. Stores the user,
    the liked product, and the time the like was created.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    liked_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the like, showing the user and
        the product they liked.
        """
        return f"{self.user.username} likes {self.liked_product.name}"
