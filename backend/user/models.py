from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, default="")
    image = models.ImageField(upload_to="profile_image", blank=True)


class SocialLink(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    user = models.ForeignKey(
        to=UserProfile, related_name="user_profile", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
