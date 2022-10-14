from rest_framework import routers

from .viewsets import AdvocateViewSet

router = routers.DefaultRouter()

router.register(r'', AdvocateViewSet, basename='advocates')

urlpatterns = router.urls
