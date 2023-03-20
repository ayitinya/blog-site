from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tag, BlogPost


# Create your tests here.
class BlogPostTests(APITestCase):
    def test_create_blogpost(self):
        url = reverse("blogpost-list")
        data = {
            "title": "My first blogpost",
            "subtitle": "My first subtitle",
            "body": "My first body",
            "author": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(BlogPost.objects.get().title, "My first blogpost")

    def test_create_tag(self):
        url = reverse("tag-list")
        data = {"name": "My first tag", "blogpost": [1]}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.get().name, "My first tag")

    def test_create_blogpost_with_tag(self):
        url = reverse("blogpost-list")
        data = {
            "title": "My first blogpost",
            "subtitle": "My first subtitle",
            "body": "My first body",
            "author": 1,
            "tags": [1],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(BlogPost.objects.get().title, "My first blogpost")
        self.assertEqual(BlogPost.objects.get().tags.count(), 2)

    def test_get_blogpost(self):
        url = reverse("blogpost-list")
        data = {
            "title": "My first blogpost",
            "subtitle": "My first subtitle",
            "body": "My first body",
            "author": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(BlogPost.objects.get().title, "My first blogpost")
        url = reverse("blogpost-detail", args=[1])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "My first blogpost")


class TagTests(APITestCase):
    def test_create_tag(self):
        url = reverse("tag-list")
        data = {"name": "My first tag", "blogpost": [1]}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.get().name, "My first tag")

    def test_get_tag(self):
        url = reverse("tag-list")
        data = {"name": "My first tag", "blogpost": [1]}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.get().name, "My first tag")
        url = reverse("tag-detail", args=[1])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "My first tag")
