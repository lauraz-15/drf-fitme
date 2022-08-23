from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
from main.permissions import isOwnerOrViewOnly

class ImageList(APIView):
    """
    Display a list of all images
    """
    serializer_class = ImageSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(
            images, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):

        serializer = ImageSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):
    """
    Display an individual image and account details
    """
    serializer_class = ImageSerializer
    permission_classes  = [isOwnerOrViewOnly]
    def get_object(self, pk):
        try:
            account = Image.objects.get(pk=pk)
            self.check_object_permissions(self.request, image)
            return image
        except Image.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(
            image, context={'request': request}
            )
        return Response(serializer.data)