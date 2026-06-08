from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .forms import ChecklistItemForm
from .models import ChecklistItem

from apps.trips.models import Trip

def checklist_list(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    items = trip.checklist_items.all()

    form = ChecklistItemForm()

    context = {
        "trip": trip,
        "items": items,
        "form": form,
    }

    return render(
        request,
        "checklists/list.html",
        context
    )

def add_checklist_item(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    if request.method == "POST":

        form = ChecklistItemForm(request.POST)

        if form.is_valid():

            item = form.save(commit=False)

            item.trip = trip

            item.save()

    return redirect(
        "checklist_list",
        trip_id=trip.id
    )

def toggle_checklist_item(
    request,
    item_id
):

    item = get_object_or_404(
        ChecklistItem,
        id=item_id
    )

    item.completed = not item.completed

    item.save()

    return redirect(
        "checklist_list",
        trip_id=item.trip.id
    )

def delete_checklist_item(
    request,
    item_id
):

    item = get_object_or_404(
        ChecklistItem,
        id=item_id
    )

    trip_id = item.trip.id

    item.delete()

    return redirect(
        "checklist_list",
        trip_id=trip_id
    )