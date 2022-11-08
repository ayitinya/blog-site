from rest_framework import serializers

from blog.models import BlogPost
from user.serializers import UserProfileSerializer


class BlogPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)
    first_name = serializers.CharField(source='author.first_name', read_only=True)
    last_name = serializers.CharField(source='author.last_name', read_only=True)


    class Meta:
        model = BlogPost
        fields = '__all__'
