from apps.links.api.serializers import LinkSerializer
from apps.links.models import Link
from rest_framework import viewsets


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
