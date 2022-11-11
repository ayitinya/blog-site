from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    pass


class SavedBlogs(models.Model):
    blogs = models.ManyToManyField(to="blog.BlogPost")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
