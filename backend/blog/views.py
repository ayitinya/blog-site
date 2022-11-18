from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
