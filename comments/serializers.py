from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    account_id = serializers.ReadOnlyField(source='owner.account.id')
    account_image = serializers.ReadOnlyField(source='owner.account.image.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

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