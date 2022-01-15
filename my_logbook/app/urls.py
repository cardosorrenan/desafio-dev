from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("upload_cnab", views.upload_cnab, name="upload_cnab"),
    path("manage_cnab", views.manage_cnab, name="manage_cnab"),
]