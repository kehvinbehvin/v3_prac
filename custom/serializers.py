from .models import Messages
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.HyperlinkedRelatedField(many=True, view_name='user-all', read_only=True)
    # recipient = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    class Meta:
        # The model it will serialize
        model = Messages
        # the fields that should be included in the serialized output
        fields = ['id', 'sender', 'recipient','message']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # The model it will serialize
        model = User
        # the fields that should be included in the serialized output
        fields = ['id', 'username']
        depth = 1
