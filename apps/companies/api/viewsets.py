
from apps.companies.api.serializers import CompanySerializer
from apps.companies.models import Company
from rest_framework.viewsets import ModelViewSet


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            company = serializer.instance
            company.href = f'http://localhost:8000/companies/{company.id}/'
            company.save()
            return company
