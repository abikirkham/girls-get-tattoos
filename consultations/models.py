from django.db import models
from django.contrib.auth.models import User


class ConsultationInterest(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation interest by {self.user.username} on {self.preferred_date}"
