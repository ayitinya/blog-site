from django.contrib import admin
from .models import UserProfile, SocialLink

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    pass