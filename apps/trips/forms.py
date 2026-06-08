from django import forms
from .models import Trip


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip

        fields = [
            "title",
            "destination",
            "description",
            "cover_image",
            "start_date",
            "end_date",
            "budget",
        ]

        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }