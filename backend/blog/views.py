from rest_framework import viewsets
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
