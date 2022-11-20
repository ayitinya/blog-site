from django.db import models
from user.models import UserProfile

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(default="", max_length=100, blank=True)
    body = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Tag(models.Model):
    name = models.CharField(max_length=20)
    blogpost = models.ManyToManyField(to=BlogPost, related_name="tags")

    def __str__(self):
        return self.name
