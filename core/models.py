from django.db import models
from users.models import CustomUser

from .validators import audio_validator


class Track(models.Model):
    title = models.CharField(
        verbose_name="Название трека",
        max_length=256
    )
    author = models.CharField(
        verbose_name="Автор трека",
        max_length=256
    )
    track = models.FileField(
        upload_to = "static/music/",
        validators=[audio_validator]
    )
    uploaded_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"


class Playlist(models.Model):
    title = models.CharField(
        verbose_name="Название плейлиста",
        max_length=256,
    )
    description = models.CharField(
        verbose_name="Описание плейлиста",
        max_length=500
    )

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлисты"