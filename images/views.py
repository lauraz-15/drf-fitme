from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer

class ImageList(APIView):
    """
    Display a list of all images
    """
    serializer_class = ImageSerializer
    
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