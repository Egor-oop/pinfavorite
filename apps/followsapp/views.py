from rest_framework import viewsets, mixins, status
from rest_framework.views import Response
from django.db import models

from .models import Follow
from .serializers import FollowSerializer


class FollowViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            follow = Follow.objects.get(follower=self.request.user,
                                        following_to=serializer.validated_data['following_to'])
            if follow.follower == self.request.user and \
                    follow.following_to == serializer.validated_data['following_to']:
                return Response({'Forbidden': 'This following already exists'}, status=status.HTTP_403_FORBIDDEN)
        except models.ObjectDoesNotExist:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save(follower=self.request.user)
