import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import Track
from .forms import AddTrackForm, UpdatePhotoProfileForm
from users.models import CustomUser

def home(request) -> render:
    """Главная страница."""
    tracks = Track.objects.all()
    # print(tracks[0].track)
    return render(request, "index.html", {"tracks": tracks})


def add_track(request) -> render:
    form = AddTrackForm()
    if request.method == "POST":
        form = AddTrackForm(request.POST, request.FILES)
        if form.is_valid():
            track_title = request.POST.get("name")
            track_author = request.POST.get("author")
            music = request.FILES["music"]
            uploaded_user = request.user

            Track.objects.create(title=track_title, author=track_author, \
                                    track=music, uploaded_user=uploaded_user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("form not valid")
        
    return render(request, "add_track.html", {"form": form})


def profile(request, user_id: int) -> render:
    user = CustomUser.objects.filter(id=user_id)
    if request.method == "POST":
        form = UpdatePhotoProfileForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = request.FILES["avatar"]
            fs = FileSystemStorage(location="static/images/user_avatars")
            
            fs.save(avatar.name, avatar)

            user.update(avatar=avatar.name)
            
            return HttpResponse("Ok")
        else:
            return HttpResponse("form not valid")
    else:
        form = UpdatePhotoProfileForm()
        return render(request, "profile.html", {"usr": user[0], "form": form})