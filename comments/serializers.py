from rest_framework import serializers
from .models import Image


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    account_id = serializers.ReadOnlyField(source='owner.account.id')
    account_image = serializers.ReadOnlyField(source='owner.account.image.url')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'account_id',
            'account_image', 'image', 'created_on', 'updated_on', 'text',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Detail view Comment serializer
    Image is a read only field so that we dont have to get it repeatedly
    """
    image = serializers.ReadOnlyField(source='image.id')