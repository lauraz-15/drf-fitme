from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Account
        fields = [
            'id', 'created_on', 'updated_on', 'owner', 'username',
            'current_weight', 'goal_weight', 'weight_private',
            'content', 'image', 'is_owner'
        ]
