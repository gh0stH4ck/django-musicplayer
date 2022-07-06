from django.urls import path

from .views import home, add_track, profile

urlpatterns = [
    path("", home, name="home"),
    path("add_track", add_track, name="add_track"),
    path("profile/<int:user_id>", profile, name="profile"),
]

