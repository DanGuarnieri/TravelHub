from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.trips.models import Trip
from .models import TravelDocument
from .forms import TravelDocumentForm

# ==========================================
# 🪪 DOCUMENTOS PESSOAIS (GLOBAIS)
# ==========================================

@login_required
def global_documents_dashboard(request):
    # Filtra apenas os documentos do usuário logado que NÃO possuem viagem (trip__isnull=True)
    documents = TravelDocument.objects.filter(owner=request.user, trip__isnull=True).order_by('-uploaded_at')
    form = TravelDocumentForm()

    return render(
        request,
        "documents/global_documents.html",
        {
            "documents": documents,
            "form": form,
        }
    )

@login_required
def upload_global_document(request):
    if request.method == "POST":
        form = TravelDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user # Associa o documento ao usuário logado
            # document.trip permanece vazio (None)
            document.save()
            messages.success(request, "Documento pessoal guardado com sucesso!")
            
    return redirect("global_documents_dashboard")


# ==========================================
# ✈️ DOCUMENTOS DA VIAGEM
# ==========================================

@login_required
def document_dashboard(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, owner=request.user)
    documents = trip.documents.all().order_by('-uploaded_at')
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

@login_required
def upload_document(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, owner=request.user)

    if request.method == "POST":
        form = TravelDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.trip = trip
            document.owner = request.user # CRÍTICO: Agora que alteramos o model, o owner é obrigatório aqui também!
            document.save()
            messages.success(request, "Documento anexado à viagem com sucesso!")

    return redirect("document_dashboard", trip_id=trip.id)


# ==========================================
# 🗑️ EXCLUSÃO INTELIGENTE (COMPARTILHADA)
# ==========================================

@login_required
def delete_document(request, document_id):
    # Garante que o usuário só pode apagar os PRÓPRIOS documentos
    document = get_object_or_404(TravelDocument, id=document_id, owner=request.user)
    
    # Salva o ID da viagem temporariamente (se existir)
    trip_id = document.trip.id if document.trip else None
    
    document.delete()
    messages.success(request, "Documento excluído.")

    # Redirecionamento condicional: Volta para onde o usuário estava
    if trip_id:
        return redirect("document_dashboard", trip_id=trip_id)
    else:
        return redirect("global_documents_dashboard")