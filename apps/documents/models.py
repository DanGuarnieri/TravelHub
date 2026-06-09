from django.db import models
from django.conf import settings # Importante para referenciar o User
from apps.trips.models import Trip

class TravelDocument(models.Model):
    CATEGORY_CHOICES = [
        ("passport", "Passaporte"),
        ("id_card", "Identidade/RG/CNH"), # Nova categoria para documentos pessoais
        ("insurance", "Seguro"),
        ("hotel", "Hotel"),
        ("flight", "Passagem"),
        ("train", "Trem"),
        ("ticket", "Ingresso"),
        ("other", "Outros"),
    ]

    # 1. NOVO: O dono do documento. Obrigatório para documentos globais.
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    # 2. ALTERADO: A viagem agora é opcional. 
    # Se for nulo, significa que é um documento Pessoal/Global.
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="documents",
        null=True,
        blank=True
    )

    title = models.CharField(max_length=255)
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    
    file = models.FileField(
        upload_to="documents/"
    )
    
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title