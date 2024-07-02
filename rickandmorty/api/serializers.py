from rest_framework import serializers

from locations.models import Character, Episode, Location


class MinLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('name', 'url')


class CharacterSerializer(serializers.ModelSerializer):
    location = MinLocationSerializer()
    origin = MinLocationSerializer()
    episodes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Character
        fields = (
            'id',
            'location',
            'origin',
            'name',
            'status',
            'species',
            'type',
            'gender',
            'image',
            'url',
            'created',
            'episodes',
        )


class LocationSerializer(serializers.ModelSerializer):
    residents = serializers.SlugRelatedField(
        read_only=True,
        slug_field='url',
        source='characters_location',
        many=True
    )

    class Meta:
        model = Location
        fields = (
            'id',
            'name',
            'type',
            'dimension',
            'url',
            'created',
            'residents',
        )


class EpisodeSerializer(serializers.ModelSerializer):
    characters = serializers.StringRelatedField(many=True)

    class Meta:
        model = Episode
        fields = (
            'id',
            'name',
            'air_date',
            'episode',
            'url',
            'created',
            'characters',
        )
