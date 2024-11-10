from django.db import models

class Consultation(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class ConsultationAvailability(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='availabilities', on_delete=models.CASCADE)
    available_date = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.consultation.name} - {self.available_date}"

    class Meta:
        unique_together = ('consultation', 'available_date')

class ConsultationBooking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    consultation_date = models.ForeignKey(ConsultationAvailability, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.consultation.name} - {self.consultation_date.available_date}"