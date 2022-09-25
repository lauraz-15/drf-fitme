from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    """
    Image model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id}'
