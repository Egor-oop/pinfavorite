from rest_framework import viewsets

from .serializers import PinSerializer
from .models import Pin
from apps.usersapp.permissions import IsOwnerOrReadOnly


class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
