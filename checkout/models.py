"""
Checkout models for managing orders and line items in the e-commerce platform.
"""

import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Represents an order placed by a customer.
    Includes customer details, delivery information, and order totals.
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID."""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        including delivery costs if applicable.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))["lineitem_total__sum"] or 0
        )
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the save method to set the order number if not already set.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """String representation of the order."""
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represents a single line item in an order.
    Contains product, quantity, and total cost for the item.
    """

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="lineitems"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate the line item total
        and update the order total.
        """
        if isinstance(self.quantity, str):
            try:
                self.quantity = int(self.quantity)
            except ValueError:
                raise ValueError("Quantity must be an integer.")

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """String representation of the line item."""
        return f"SKU {self.product.sku} on order {self.order.order_number}"
