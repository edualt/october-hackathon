from apps.advocates.models import Advocate
from apps.companies.models import Company
from apps.links.api.serializers import LinkSerializer
from rest_framework import serializers


class AdvocateSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    companies = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), many=True)

    class Meta:
        model = Advocate
        fields = ['id', 'profile_pic', 'username', 'name', 'short_bio', 'long_bio', 'companies', 'links']
        depth = 1

    

