from django.urls import path 
from .views import dashboard, create_trip, trip_detail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path("viagens/nova/", create_trip, name="create_trip"),
        path(
        'viagens/<int:trip_id>/',
        trip_detail,
        name='trip_detail'
    ),

]