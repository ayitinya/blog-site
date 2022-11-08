from rest_framework import routers
 
from blog.views import BlogPostViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogPostViewSet)

urlpatterns = router.urls
