from rest_framework import serializers
from webapp.models import RawData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = ('id', 'winddir')