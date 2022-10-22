
from os import environ

import environ
from apps.companies.api.serializers import CompanySerializer
from apps.companies.models import Company
from rest_framework.viewsets import ModelViewSet

env = environ.Env()
environ.Env.read_env()


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            company = serializer.instance
            company.href = env.str('URL_HOST') + 'companies/' + str(company.id)
            company.save()
            return company
