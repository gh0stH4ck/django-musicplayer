from django import forms

from .validators import audio_validator
from users.models import CustomUser

class AddTrackForm(forms.Form):
    name = forms.CharField(label="Название трека", max_length=256)
    author = forms.CharField(label="Автор", max_length=256)
    music = forms.FileField(label="Выберите файл", validators=[audio_validator])


class UpdatePhotoProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("avatar", )