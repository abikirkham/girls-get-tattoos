from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the contact message,
        showing the sender's name and the read status.
        """
        return (
            f"Message from {self.name} "
            f"({'Read' if self.read else 'Unread'})"
        )
