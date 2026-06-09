from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.trips.models import Trip
from .models import TravelPhoto
from .forms import TravelPhotoForm
from django.contrib.auth.decorators import login_required

@login_required
def gallery_dashboard(request, trip_id):
    # Busca a viagem correspondente
    trip = get_object_or_404(Trip, id=trip_id)
    
    # Busca as fotos organizadas pelas mais recentes usando o related_name="photos"
    photos = trip.photos.all().order_by('-taken_at')

    if request.method == 'POST':
        # IMPORTANTE: request.FILES é obrigatório para receber imagens
        form = TravelPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.trip = trip # Atrela a foto à viagem atual
            photo.save()
            messages.success(request, 'Memória guardada com sucesso!')
            return redirect('gallery_dashboard', trip_id=trip.id)
    else:
        form = TravelPhotoForm()

    context = {
        'trip': trip,
        'photos': photos,
        'form': form
    }
    return render(request, 'gallery/gallery.html', context)
@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(TravelPhoto, id=photo_id)
    trip_id = photo.trip.id
    photo.delete()
    messages.success(request, 'Foto excluída do álbum.')
    return redirect('gallery_dashboard', trip_id=trip_id)
@login_required
def toggle_favorite(request, photo_id):
    photo = get_object_or_404(TravelPhoto, id=photo_id)
    photo.favorite = not photo.favorite # Inverte o status atual
    photo.save()
    return redirect('gallery_dashboard', trip_id=photo.trip.id)