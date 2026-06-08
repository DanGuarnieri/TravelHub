from django.db import models

from apps.trips.models import Trip

class TravelDocument(models.Model):

    CATEGORY_CHOICES = [

        ("passport", "Passaporte"),
        ("insurance", "Seguro"),
        ("hotel", "Hotel"),
        ("flight", "Passagem"),
        ("train", "Trem"),
        ("ticket", "Ingresso"),
        ("other", "Outros"),
    ]

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    title = models.CharField(
        max_length=255
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    file = models.FileField(
        upload_to="documents/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title