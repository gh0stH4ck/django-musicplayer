from django.urls import path

from .views import home, add_track

urlpatterns = [
    path("", home, name="home"),
    path("add_track", add_track, name="add_track"),
]