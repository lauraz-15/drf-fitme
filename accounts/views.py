from django.db.models import Count
from rest_framework import generics, filters
from .models import Account
from .serializers import AccountSerializer
from main.permissions import isOwnerOrViewOnly

class AccountList(generics.ListAPIView):
    """
    Display a list of all accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Display an individual account and account details
    Update option provided for the Acount holders
    
    """
    permission_classes = [isOwnerOrViewOnly]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer