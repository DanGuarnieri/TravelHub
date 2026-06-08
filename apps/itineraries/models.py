from django.db import models

from apps.trips.models import Trip

class ItineraryDay(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="itinerary_days"
    )

    date = models.DateField()

    notes = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.trip.title} - {self.date}"
    
class Activity(models.Model):

    day = models.ForeignKey(
        ItineraryDay,
        on_delete=models.CASCADE,
        related_name="activities"
    )

    title = models.CharField(
        max_length=255
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    start_time = models.TimeField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title