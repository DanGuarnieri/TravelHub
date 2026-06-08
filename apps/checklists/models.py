from django.db import models

from apps.trips.models import Trip


class ChecklistItem(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="checklist_items"
    )

    title = models.CharField(
        max_length=255
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title