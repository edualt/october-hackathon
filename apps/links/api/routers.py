from rest_framework import routers

from .viewsets import LinkViewSet

router = routers.DefaultRouter()

router.register(r'', LinkViewSet, basename='links')

urlpatterns = router.urls
