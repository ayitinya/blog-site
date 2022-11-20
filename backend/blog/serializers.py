from rest_framework import serializers

from blog.models import BlogPost, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="author.username", read_only=True)
    first_name = serializers.CharField(source="author.first_name", read_only=True)
    last_name = serializers.CharField(source="author.last_name", read_only=True)
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        queryset = Tag.objects.filter(blogpost=obj.id)
        return TagSerializer(queryset, many=True).data

    class Meta:
        model = BlogPost
        fields = "__all__"
