from django.db import models
from apps.usersapp.models import CustomUser


class Pin(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
