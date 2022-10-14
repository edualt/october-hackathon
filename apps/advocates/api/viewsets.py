from apps.advocates.models import Advocate
from apps.companies.models import Company
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import AdvocateSerializer


class AdvocateViewSet(viewsets.ModelViewSet):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    
    def perform_create(self, serializer):
        company = Company.objects.get(pk=self.request.data['company'])
        serializer.save(company=company)
