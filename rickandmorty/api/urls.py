from django.urls import include, path
from rest_framework import routers

from .views import CharacterViewSet, LocationViewSet, EpisodeViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('character', CharacterViewSet, basename='character')
router.register('location', LocationViewSet, basename='location')
router.register('episode', EpisodeViewSet, basename='episode')

urlpatterns = [
    path('v1/', include(router.urls)),
]
