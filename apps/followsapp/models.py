from django.db import models
from apps.usersapp.models import CustomUser


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followings_to', blank=True)
    following_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')
