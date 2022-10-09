from rest_framework import serializers
from apps.advocates.models import Advocate

class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'