from .models import First
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class FirstSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = First
        # the fields that should be included in the serialized output
        fields = ['id', 'postalCode']