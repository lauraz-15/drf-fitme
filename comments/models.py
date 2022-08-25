from django.db import models
from django.contrib.auth.models import User
from images.models import Image


class Comment(models.Model):
    """
    Comment model, related to User and Image
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content