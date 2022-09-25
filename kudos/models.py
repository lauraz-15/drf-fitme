from django.db import models
from django.contrib.auth.models import User
from images.models import Image


class Kudos(models.Model):
    """
    Kudos model, related to User and Image.
    'unique_together' ensures that one user can't add kudos
    to the same image twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='kudos')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'image']

    def __str__(self):
        return f'{self.owner} {self.image}'
