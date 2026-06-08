from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from apps.trips.models import Trip

from .models import (
    ItineraryDay,
    Activity
)

from .forms import (
    ItineraryDayForm,
    ActivityForm
)

def itinerary_dashboard(
    request,
    trip_id
):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    days = trip.itinerary_days.prefetch_related(
        "activities"
    )

    context = {
        "trip": trip,
        "days": days,
        "day_form": ItineraryDayForm(),
    }

    return render(
        request,
        "itineraries/dashboard.html",
        context
    )

def add_day(
    request,
    trip_id
):

    trip = get_object_or_404(
        Trip,
        id=trip_id
    )

    if request.method == "POST":

        form = ItineraryDayForm(
            request.POST
        )

        if form.is_valid():

            day = form.save(
                commit=False
            )

            day.trip = trip

            day.save()

    return redirect(
        "itinerary_dashboard",
        trip_id=trip.id
    )

def add_activity(
    request,
    day_id
):

    day = get_object_or_404(
        ItineraryDay,
        id=day_id
    )

    if request.method == "POST":

        form = ActivityForm(
            request.POST
        )

        if form.is_valid():

            activity = form.save(
                commit=False
            )

            activity.day = day

            activity.save()

    return redirect(
        "itinerary_dashboard",
        trip_id=day.trip.id
    )