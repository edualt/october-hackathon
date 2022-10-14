from rest_framework import routers

from .viewsets import CompanyViewSet

router = routers.DefaultRouter()

router.register(r'', CompanyViewSet, basename='companies')

urlpatterns = router.urls
