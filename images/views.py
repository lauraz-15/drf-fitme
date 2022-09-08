from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Image
from .serializers import ImageSerializer
from main.permissions import isOwnerOrViewOnly

class ImageList(generics.ListAPIView):
    """
    Display a list of all images
    Add a new image if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Image.objects.annotate(
        comments_count=Count('comment', distinct=True),
        kudos_count=Count('kudos', distinct=True),
    ).order_by('-created_on')
    serializer_class = ImageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'comments_count',
        'kudos_count',
        'kudos__created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display an individual image
    Update and Delete option visible for image owners
    """
    permission_classes = [isOwnerOrViewOnly]
    queryset = Image.objects.annotate(
        comments_count=Count('comment', distinct=True),
        kudos_count=Count('kudos', distinct=True),
    ).order_by('-created_on')
    serializer_class = ImageSerializer