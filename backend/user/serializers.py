from rest_framework import serializers

from .models import UserProfile, SocialLink


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ["name", "url"]


class UserProfileSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "first_name", "last_name", "bio", "image", "social_links"]

    def get_social_links(self, obj):
        queryset = SocialLink.objects.filter(user=obj.id)
        return SocialLinkSerializer(queryset, many=True).data
