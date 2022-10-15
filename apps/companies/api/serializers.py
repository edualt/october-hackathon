from apps.advocates.api.serializers import AdvocateSerializer
from apps.advocates.models import Advocate
from apps.companies.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Company
        fields = ['id', 'name', 'href', 'summary', 'advocates']
        extra_kwargs = {
            'href': {'read_only': True}
        }
        depth = 1
    
