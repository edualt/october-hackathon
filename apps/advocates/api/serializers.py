from apps.advocates.models import Advocate
from rest_framework import serializers


class AdvocateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio', 'years_of_experience', 'company', 'links']
        depth = 1
