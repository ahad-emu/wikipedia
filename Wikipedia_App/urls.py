from django.urls import path
from Wikipedia_App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("show/", views.show, name="show"),
    path("about/", views.about, name="about"),
    path("insert/", views.insert, name="insert"),
    path("upload/", views.upload, name="upload"),
    path("details/<Item_id>", views.details, name="details"),
    path("delete/<Item_id>", views.delete, name="delete"),
    path("edit/<Item_id>", views.edit, name="edit"),
    path("edit_upload/<Item_id>", views.edit_upload, name="edit_upload"),
]
