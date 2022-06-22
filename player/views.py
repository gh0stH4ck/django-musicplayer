from django.http import HttpResponse
from django.shortcuts import render
import os

from .models import Track
from .forms import AddTrackForm

def home(request) -> render:
    """Главная страница."""
    tracks = Track.objects.all()
    return render(request, "index.html", {"tracks": tracks})


def add_track(request) -> render:
    form = AddTrackForm()
    if request.method == "POST":
        form = AddTrackForm(request.POST, request.FILES)
        if form.is_valid():
            track_title = request.POST.get("name")
            track_author = request.POST.get("author")
            music = request.FILES["music"]

            Track.objects.create(title=track_title, author=track_author, \
                                    track=music)
            return HttpResponse("track upload successful")
        else:
            return HttpResponse("form no valid")
    return render(request, "add_track.html", {"form": form})