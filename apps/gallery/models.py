from django.db import models
from apps.trips.models import Trip

# Create your models here.
class TravelPhoto(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    image = models.ImageField(
        upload_to="trip_photos/"
    )

    caption = models.CharField(
        max_length=255,
        blank=True
    )

    taken_at = models.DateTimeField(
        auto_now_add=True
    )

    favorite = models.BooleanField(
        default=False
    )