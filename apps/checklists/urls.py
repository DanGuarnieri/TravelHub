from django.urls import path

from . import views

urlpatterns = [

    path(
        "viagens/<int:trip_id>/checklist/",
        views.checklist_list,
        name="checklist_list"
    ),

    path(
        "viagens/<int:trip_id>/checklist/add/",
        views.add_checklist_item,
        name="add_checklist_item"
    ),

    path(
        "checklist/<int:item_id>/toggle/",
        views.toggle_checklist_item,
        name="toggle_checklist_item"
    ),

    path(
        "checklist/<int:item_id>/delete/",
        views.delete_checklist_item,
        name="delete_checklist_item"
    ),

]