from .models import Trip
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TripForm

def trip_detail(request, trip_id):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )
    checklist_count = trip.checklist_items.count()

    completed_count = trip.checklist_items.filter(
        completed=True
    ).count()


    context = {
    "trip": trip,
    "checklist_count": checklist_count,
    "completed_count": completed_count,
    }

    return render(
        request,
        "trips/trip_detail.html",
        context
    )

def dashboard(request):

    trips = Trip.objects.all()


    context = {
    "trips": trips,
    "total_trips": trips.count(),
    }

    return render(
        request,
        "trips/dashboard.html",
        context
    )

def create_trip(request):

    if request.method == "POST":

        form = TripForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            trip = form.save(commit=False)

            trip.owner = request.user

            trip.save()

            return redirect("dashboard")

    else:

        form = TripForm()

    return render(
        request,
        "trips/create_trip.html",
        {
            "form": form
        }
    )