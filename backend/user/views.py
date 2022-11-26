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
    def blogs(self, request, *args, pk=None, **kwargs):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))
        queryset = BlogPost.objects.all()
        blogs = queryset.filter(author=pk)
        serializer = BlogPostSerializer(blogs[offset : offset + limit], many=True)
        return Response(
            {
                "count": blogs.count(),
                "next": len(blogs) > limit,
                "results": serializer.data,
            }
        )
