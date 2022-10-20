from apps.advocates.models import Advocate
from apps.companies.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    advocates = serializers.PrimaryKeyRelatedField(queryset=Advocate.objects.all(), many=True)
        
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo','href', 'summary', 'advocates']
        extra_kwargs = {
            'href': {'read_only': True}
        }
        depth = 1
