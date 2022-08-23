from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer

class ImageList(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(
            images, many=True, context={'request': request}
        )
        return Response(serializer.data)
        