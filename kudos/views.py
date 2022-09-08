from rest_framework import generics, permissions
from main.permissions import isOwnerOrViewOnly
from .models import Kudos
from .serializers import KudosSerializer


class KudosList(generics.ListCreateAPIView):
    """
    List all kudos.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Kudos.objects.all()
    serializer_class = KudosSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



