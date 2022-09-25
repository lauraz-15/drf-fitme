from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Account(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(max_length=255, blank=True)
    current_weight = models.PositiveIntegerField(null=True, blank=True)
    goal_weight = models.PositiveIntegerField(null=True, blank=True)
    weight_private = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../user-logged_giqn26.svg'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s account"


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(owner=instance)

post_save.connect(create_account, sender=User)
