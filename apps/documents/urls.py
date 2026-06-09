from django.urls import path
from . import views

urlpatterns = [
    # Rotas de Documentos Globais (Sem Viagem)
    path('meus-documentos/', views.global_documents_dashboard, name='global_documents_dashboard'),
    path('meus-documentos/upload/', views.upload_global_document, name='upload_global_document'),

    # Rotas de Documentos da Viagem
    path('viagem/<int:trip_id>/documentos/', views.document_dashboard, name='document_dashboard'),
    path('viagem/<int:trip_id>/documentos/upload/', views.upload_document, name='upload_document'),
    
    # Rota de Exclusão Única
    path('documento/<int:document_id>/excluir/', views.delete_document, name='delete_document'),
]