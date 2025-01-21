from django.db import models


class Consultation(models.Model):
    """
    Represents a consultation service offered in the e-commerce platform.

    Attributes:
        sku (str): The stock keeping unit for the consultation.
        name (str): The name of the consultation.
        description (str): A detailed description of the consultation.
        price (Decimal): The price of the consultation.
        rating (Decimal): Average customer rating of the consultation.
        image_url (str): URL of the consultation's image.
        image (ImageField): Image uploaded for the consultation.
    """

    sku = models.CharField(
        max_length=254, null=True, blank=True
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.URLField(
        max_length=1024, null=True, blank=True
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """String representation of a Consultation instance."""
        return self.name


class ConsultationAvailability(models.Model):
    consultation = models.ForeignKey(
        Consultation, related_name='availabilities', on_delete=models.CASCADE
    )
    available_date = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        """String representation of a ConsultationAvailability instance."""
        return f"{self.consultation.name} - {self.available_date}"

    class Meta:
        unique_together = ('consultation', 'available_date')


class ConsultationBooking(models.Model):
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    consultation = models.ForeignKey(
        Consultation, on_delete=models.CASCADE
    )
    consultation_date = models.ForeignKey(
        ConsultationAvailability, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of a ConsultationBooking instance."""
        return (
            f"{self.user.username} - {self.consultation.name} - "
            f"{self.consultation_date.available_date}"
        )
