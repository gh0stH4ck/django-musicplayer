import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Track
from .forms import AddTrackForm
from musicplayer.settings import BASE_DIR

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
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("form not valid")
    return render(request, "add_track.html", {"form": form})