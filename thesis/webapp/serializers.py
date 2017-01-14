from rest_framework import serializers
from webapp.models import RawData

class DataSerializer(serializers.ModelSerializer):
    #plantdata = serializers.PrimaryKeyRelatedField(many=True, queryset=Record.objects.all())

    class Meta:
        model = RawData
        fields = ('id', 'winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp')