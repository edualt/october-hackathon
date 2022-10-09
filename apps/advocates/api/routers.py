from rest_framework import routers
from .viewsets import AdvocateViewSet

router = routers.DefaultRouter()

router.register(r'advocates', AdvocateViewSet)

urlpatterns = router.urls