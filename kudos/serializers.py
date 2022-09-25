from rest_framework import serializers
from .models import Kudos
from django.db import IntegrityError


class KudosSerializer(serializers.ModelSerializer):
    """
    Serializer for the Kudos model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Kudos
        fields = [
            'id', 'owner', 'created_on', 'image',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate kudos'
            })
