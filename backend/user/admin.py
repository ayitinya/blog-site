from django.contrib import admin
from user.models import SavedBlogs, UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(SavedBlogs)
class SavedBlogsAdmin(admin.ModelAdmin):
    pass