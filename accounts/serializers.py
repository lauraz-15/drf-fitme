from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Account
        fields = [
            'id', 'created_on', 'updated_on', 'owner', 'username',
            'current_weight', 'goal_weight', 'weight_private',
            'content', 'image'
        ]
