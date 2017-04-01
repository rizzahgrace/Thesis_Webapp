from rest_framework import serializers
from webapp.models import RawData_AMPS, Owner
from django.contrib.auth.models import User

class DataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.owner.last_name')
    class Meta:
        model = RawData_AMPS
        fields = ('id', 'grid', 'load', 'address', 'owner')

class OwnerSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Owner.objects.all())

    class Meta:
        model = Owner
        fields = ('id', 'last_name', 'first_name', 'location')