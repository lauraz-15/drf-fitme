from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to owner and folowed.
    unique_together ensures that User can only follow
    another user once.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
    
