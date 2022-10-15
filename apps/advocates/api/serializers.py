from apps.advocates.models import Advocate
from apps.companies.models import Company
from rest_framework import serializers


class AdvocateSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio', 'years_of_experience', 'links', 'company']
        depth = 1
