from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("paper/", views.join, name="join"),
]