from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    account_id = serializers.ReadOnlyField(source='owner.account.id')
    account_image = serializers.ReadOnlyField(source='owner.account.image.url')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Image
        fields = [
            'id', 'owner', 'is_owner', 'account_id', 
            'account_image', 'created_on', 'updated_on', 'owner',
            'description', 'picture'
        ]