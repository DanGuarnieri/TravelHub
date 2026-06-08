from datetime import date
from django.conf import settings
from django.db import models


class Trip(models.Model):

    STATUS_CHOICES = [
        ("planning", "Planejamento"),
        ("travelling", "Em viagem"),
        ("finished", "Finalizada"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    destination = models.CharField(max_length=200)

    start_date = models.DateField()

    end_date = models.DateField()

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    cover_image = models.ImageField(
        upload_to="trip_covers/",
        blank=True,
        null=True
        )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planning"
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def days_remaining(self):
        return max(
            (self.start_date - date.today()).days,
            0
        )

    def __str__(self):
        return self.title
    
    cover_image = models.ImageField(
    upload_to="trip_covers/",
    blank=True,
    null=True
    )

    country_flag = models.CharField(
        max_length=10,
        blank=True,
        default=""
    )

    @property
    def preparation_progress(self):

        total = 4

        completed = 0

        if self.budget > 0:
            completed += 1

        if self.start_date:
            completed += 1

        if self.end_date:
            completed += 1

        if self.description:
            completed += 1

        return int((completed / total) * 100)
    
    @property
    def total_income(self):

        total = self.transactions.filter(
            transaction_type="income"
        ).aggregate(
            models.Sum("amount")
        )["amount__sum"]

        return total or 0
    @property
    def total_expense(self):

        total = self.transactions.filter(
            transaction_type="expense"
        ).aggregate(
            models.Sum("amount")
        )["amount__sum"]

        return total or 0
    @property
    def available_balance(self):

        return self.total_income - self.total_expense