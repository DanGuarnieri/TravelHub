from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction

        fields = [
            "transaction_type",
            "category",
            "description",
            "amount",
            "transaction_date",
        ]

        widgets = {
            "transaction_date": forms.DateInput(
                attrs={"type": "date"}
            )
        }