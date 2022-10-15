from apps.advocates.models import Advocate
from apps.companies.models import Company
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import AdvocateSerializer


class AdvocateViewSet(viewsets.ModelViewSet):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer



