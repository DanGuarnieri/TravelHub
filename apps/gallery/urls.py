from django.urls import path
from . import views

urlpatterns = [
    path('trip/<int:trip_id>/gallery/', views.gallery_dashboard, name='gallery_dashboard'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    path('photo/<int:photo_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]