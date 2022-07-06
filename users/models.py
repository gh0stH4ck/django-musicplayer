from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(
        verbose_name="Изображение",
        upload_to="media/uploads/images/user_avatars/",
        null=True,
    )