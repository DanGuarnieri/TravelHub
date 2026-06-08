from django.urls import path

from . import views

urlpatterns = [

    path(
        "viagens/<int:trip_id>/documentos/",
        views.document_dashboard,
        name="document_dashboard"
    ),

    path(
        "viagens/<int:trip_id>/documentos/upload/",
        views.upload_document,
        name="upload_document"
    ),

    path(
        "documentos/<int:document_id>/delete/",
        views.delete_document,
        name="delete_document"
    ),
]