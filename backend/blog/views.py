from rest_framework import viewsets
from .models import BlogPost, Tag
from .serializers import BlogPostSerializer, TagSerializer


# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    
    
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
