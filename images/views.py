from rest_framework import generics, permissions
from .models import Image
from .serializers import ImageSerializer
from main.permissions import isOwnerOrViewOnly

class ImageList(generics.ListAPIView):
    """
    Display a list of all images
    Add a new image if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display an individual image
    Update and Delete option visible for image owners
    """
    permission_classes = [isOwnerOrViewOnly]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer