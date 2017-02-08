from rest_framework import serializers
from webapp.models import RawData_Weather

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData_Weather
        fields = ('id', 'winddir')