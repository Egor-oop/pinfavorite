"""pinfavorite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from apps.usersapp.views import UserViewSet, RegisterUserAPIView, CustomAuthToken, PersonalAccountViewSet
from apps.pinsapp.views import PinViewSet
from apps.packsapp.views import PackViewSet
from apps.followsapp.views import FollowViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'personal', PersonalAccountViewSet, basename='personal')
router.register(r'pins', PinViewSet, basename='pins')
router.register(r'packs', PackViewSet, basename='packs')
router.register(r'follows', FollowViewSet, basename='follows')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api/register/', RegisterUserAPIView.as_view()),
    path('api/login/', CustomAuthToken.as_view()),
]
