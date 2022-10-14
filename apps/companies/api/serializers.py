from apps.advocates.api.serializers import AdvocateSerializer
from apps.companies.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    # advocates = AdvocateSerializer(many=True)
    
    class Meta:
        model = Company
        fields = ['id', 'name', 'href', 'summary', 'advocates']
        extra_kwargs = {
            'href': {'read_only': True}
        }
        depth = 1
