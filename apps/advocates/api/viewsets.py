from rest_framework import viewsets
from .serializers import AdvocateSerializer
from apps.advocates.models import Advocate

class AdvocateViewSet(viewsets.ModelViewSet):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
