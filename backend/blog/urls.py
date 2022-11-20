from rest_framework import routers
 
from blog.views import BlogPostViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogPostViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls
