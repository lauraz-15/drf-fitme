from rest_framework import generics, permissions
from main.permissions import isOwnerOrViewOnly
from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isOwnerOrViewOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer()