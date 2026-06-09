from django import forms
from .models import TravelPhoto

class TravelPhotoForm(forms.ModelForm):
    class Meta:
        model = TravelPhoto
        fields = ['image', 'caption', 'favorite']
        labels = {
            'image': 'Arquivo da Foto',
            'caption': 'Legenda (Opcional)',
            'favorite': 'Marcar como Favorita ❤️'
        }