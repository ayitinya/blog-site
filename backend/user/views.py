from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(methods=["GET"], detail=True)
    def blogs(self, request, pk=None):
        blog_posts = BlogPost.objects.filter(author=pk)
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)
