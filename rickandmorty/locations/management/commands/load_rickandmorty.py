from pprint import pprint

import requests
from django.core.management.base import BaseCommand
from locations.models import Character, Episode, Location


class Command(BaseCommand):

    def handle(self, *args, **options):

        #  Парсим Локации.
        for index in range(1, 127):
            url = f"https://rickandmortyapi.com/api/location/{index}"
            response = requests.get(url)
            response = response.json()
            Location.objects.create(
                id=response["id"],
                name=response["name"],
                type=response["type"],
                dimension=response["dimension"],
                url=response["url"],
                created=response["created"],
            )
        print("--- Location is OK ---")

        #  Парсим Персонажей.
        for index in range(1, 827):
            url = f"https://rickandmortyapi.com/api/character/{index}"
            response = requests.get(url)
            response = response.json()
            url_origin = response["origin"]["url"]
            if url_origin != "":
                id_origin = int(response["origin"]["url"].split("/")[-1])
                origin = Location.objects.get(id=id_origin)
            else:
                origin = None
            url_location = response["location"]["url"]
            if url_location != "":
                id_location = int(response["location"]["url"].split("/")[-1])
                location = Location.objects.get(id=id_location)
            else:
                location = None
            Character.objects.create(
                id=response["id"],
                name=response["name"],
                status=response["status"],
                species=response["species"],
                type=response["type"],
                gender=response["gender"],
                image=response["image"],
                url=response["url"],
                created=response["created"],
                origin=origin,
                location=location,
            )
        print("--- Character is OK ---")

        #  Парсим Эпизоды.
        for index in range(1, 52):
            url = f"https://rickandmortyapi.com/api/episode/{index}"
            response = requests.get(url)
            response = response.json()
            Episode.objects.create(
                id=response["id"],
                name=response["name"],
                air_date=response["air_date"],
                episode=response["episode"],
                url=response["url"],
                created=response["created"],
            )
            url_characters = response["characters"]
            characters = []
            for url_character in url_characters:
                id_character = int(url_character.split("/")[-1])
                characters.append(Character.objects.get(id=id_character))
            episode = Episode.objects.get(id=index)
            episode.characters.set(characters)
        print("--- Episode is OK ---")
