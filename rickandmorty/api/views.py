from locations.models import Character, Episode, Location
from rest_framework import viewsets

from .serializers import (
    CharacterSerializer,
    EpisodeSerializer,
    LocationSerializer,
)


class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
