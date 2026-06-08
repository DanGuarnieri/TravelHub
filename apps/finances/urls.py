from django.urls import path

from . import views

urlpatterns = [

    path(
        "viagens/<int:trip_id>/financeiro/",
        views.finance_dashboard,
        name="finance_dashboard"
    ),

    path(
        "viagens/<int:trip_id>/financeiro/add/",
        views.add_transaction,
        name="add_transaction"
    ),

    path(
        "financeiro/<int:transaction_id>/delete/",
        views.delete_transaction,
        name="delete_transaction"
    ),
]