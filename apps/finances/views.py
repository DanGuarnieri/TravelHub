from apps.trips.models import Trip
from .forms import TransactionForm
from .models import Transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def finance_dashboard(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, owner=request.user)
    transactions = trip.transactions.all().order_by('-transaction_date')

    # ==========================================
    # LÓGICA DO GRÁFICO (Agrupando despesas por categoria)
    # ==========================================
    
    # Substitua a linha antiga por esta, que cobre as variações de texto:
    expenses_by_category = trip.transactions.filter(
        transaction_type__in=['expense', 'Saída', 'saida', 'Saida']
    )\
        .values('category')\
        .annotate(total=Sum('amount'))\
        .order_by('-total')

    chart_labels = [item['category'] for item in expenses_by_category]
    chart_data = [float(item['total']) for item in expenses_by_category]

    form = TransactionForm()

    context = {
        'trip': trip,
        'transactions': transactions,
        'form': form,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }
    return render(request, 'finances/dashboard.html', context)

@login_required
def add_transaction(
    request,
    trip_id
):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    if request.method == "POST":

        form = TransactionForm(
            request.POST
        )

        if form.is_valid():

            transaction = form.save(
                commit=False
            )

            transaction.trip = trip

            transaction.save()

    return redirect(
        "finance_dashboard",
        trip_id=trip.id
    )
@login_required
def delete_transaction(
    request,
    transaction_id
):

    transaction = get_object_or_404(
        Transaction,
        id=transaction_id
    )

    trip_id = transaction.trip.id

    transaction.delete()

    return redirect(
        "finance_dashboard",
        trip_id=trip_id
    )