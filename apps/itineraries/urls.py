from django.urls import path

from . import views

urlpatterns = [

    path(
        "viagens/<int:trip_id>/roteiro/",
        views.itinerary_dashboard,
        name="itinerary_dashboard"
    ),

    path(
        "viagens/<int:trip_id>/roteiro/add-day/",
        views.add_day,
        name="add_day"
    ),

    path(
        "roteiro/day/<int:day_id>/add-activity/",
        views.add_activity,
        name="add_activity"
    ),
]