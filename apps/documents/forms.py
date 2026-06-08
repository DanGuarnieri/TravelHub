from django import forms

from .models import TravelDocument


class TravelDocumentForm(forms.ModelForm):

    class Meta:

        model = TravelDocument

        fields = [
            "title",
            "category",
            "file",
        ]