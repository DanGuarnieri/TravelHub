from django.db import models

from apps.trips.models import Trip

class Transaction(models.Model):

    TYPE_CHOICES = [
        ("income", "Entrada"),
        ("expense", "Saída"),
    ]

    CATEGORY_CHOICES = [
        ("flight", "Passagem"),
        ("hotel", "Hospedagem"),
        ("food", "Alimentação"),
        ("transport", "Transporte"),
        ("shopping", "Compras"),
        ("other", "Outros"),
    ]

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    description = models.CharField(
        max_length=255
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.description