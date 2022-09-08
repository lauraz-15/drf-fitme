from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_user = serializers.ReadOnlyField

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_on','followed', 'followed_user'
        ]