from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from apps.trips.models import Trip

from .forms import TransactionForm
from .models import Transaction

def finance_dashboard(
    request,
    trip_id
):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    transactions = trip.transactions.order_by(
        "-transaction_date"
    )

    form = TransactionForm()

    context = {
        "trip": trip,
        "transactions": transactions,
        "form": form,
    }

    return render(
        request,
        "finances/dashboard.html",
        context
    )

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