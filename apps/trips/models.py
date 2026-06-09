from datetime import date
from django.conf import settings
from django.db import models

class Trip(models.Model):
    STATUS_CHOICES = [
        ("planning", "Planejamento"),
        ("travelling", "Em viagem"),
        ("finished", "Finalizada"),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    
    start_date = models.DateField()
    end_date = models.DateField()
    
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Campo declarado apenas uma vez
    cover_image = models.ImageField(upload_to="trip_covers/", blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planning")
    description = models.TextField(blank=True)
    country_flag = models.CharField(max_length=10, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def days_remaining(self):
        return max((self.start_date - date.today()).days, 0)

    @property
    def preparation_progress(self):
        # 1. Progresso Base da Viagem (Peso 50%)
        base_total = 4
        base_completed = 0
        
        if self.budget > 0: base_completed += 1
        if self.description: base_completed += 1
        if self.cover_image: base_completed += 1
        if self.country_flag: base_completed += 1

        # 2. Progresso do Checklist (Peso 50%)
        checklist_progress = 0
        
        # NOTA: Ajuste 'checklist_items' para o related_name exato que você usou 
        # no modelo de Checklist (ex: self.checklists.count(), self.items.count())
        total_items = self.checklist_items.count() 
        
        if total_items > 0:
            completed_items = self.checklist_items.filter(completed=True).count()
            checklist_progress = (completed_items / total_items) * 50
            base_progress = (base_completed / base_total) * 50
        else:
            # Se a pessoa ainda não criou um checklist, 
            # os itens base representam 100% do progresso atual.
            base_progress = (base_completed / base_total) * 100

        return int(base_progress + checklist_progress)
    
    @property
    def total_income(self):
        # ATENÇÃO: Certifique-se de que no seu model 'Transaction', o valor salvo no banco é realmente "income" e "expense".
        total = self.transactions.filter(transaction_type="income").aggregate(models.Sum("amount"))["amount__sum"]
        return total or 0

    @property
    def total_expense(self):
        total = self.transactions.filter(transaction_type="expense").aggregate(models.Sum("amount"))["amount__sum"]
        return total or 0

    @property
    def available_balance(self):
        return self.total_income - self.total_expense