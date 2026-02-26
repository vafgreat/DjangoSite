from django.urls import path

from . import views

app_name = "matematika"

urlpatterns = [
    path("", views.index, name="index"),
    path("description/<int:description_id>", views.description_page, name="description")
]
