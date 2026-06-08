from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from apps.trips.models import Trip

from .models import TravelDocument
from .forms import TravelDocumentForm

def document_dashboard(
    request,
    trip_id
):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    documents = trip.documents.all()

    form = TravelDocumentForm()

    return render(
        request,
        "documents/dashboard.html",
        {
            "trip": trip,
            "documents": documents,
            "form": form,
        }
    )

def upload_document(
    request,
    trip_id
):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    if request.method == "POST":

        form = TravelDocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            document = form.save(
                commit=False
            )

            document.trip = trip

            document.save()

    return redirect(
        "document_dashboard",
        trip_id=trip.id
    )

def delete_document(
    request,
    document_id
):

    document = get_object_or_404(
        TravelDocument,
        id=document_id
    )

    trip_id = document.trip.id

    document.delete()

    return redirect(
        "document_dashboard",
        trip_id=trip_id
    )