from django import forms

from .models import (
    ItineraryDay,
    Activity
)

class ItineraryDayForm(forms.ModelForm):

    class Meta:

        model = ItineraryDay

        fields = [
            "date",
            "notes"
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

class ActivityForm(forms.ModelForm):

    class Meta:

        model = Activity

        fields = [
            "title",
            "location",
            "start_time",
            "notes"
        ]

        widgets = {
            "start_time": forms.TimeInput(
                attrs={"type": "time"}
            )
        }