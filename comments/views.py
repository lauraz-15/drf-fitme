from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from main.permissions import isOwnerOrViewOnly
from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all comments and create a comment if autheciated user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['image']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display individual comment.
    Update or delete if user is the owner.
    """
    permission_classes = [isOwnerOrViewOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
