from django.db.models import Count
from rest_framework import generics, filters
from .models import Account
from .serializers import AccountSerializer
from main.permissions import isOwnerOrViewOnly

class AccountList(generics.ListAPIView):
    """
    Display a list of all accounts
    """
    queryset = Account.objects.annotate(
        images_count=Count('owner__image', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')
    serializer_class = AccountSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'images_count',
        'followers_count=Count',
        'following_count=Count',
        'owner__followed__created_on',
        'owner__following__created_on'
    ]

class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Display an individual account and account details
    Update option provided for the Acount holders
    
    """
    permission_classes = [isOwnerOrViewOnly]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer