from django.db import models
from apps.pinsapp.models import Pin
from apps.usersapp.models import CustomUser


class Pack(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    pins = models.ManyToManyField(Pin)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
