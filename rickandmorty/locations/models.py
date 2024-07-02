from django.db import models


class Character(models.Model):
    '''Персонаж.'''

    STATUS_CHOICES = (
        ('Alive', 'Alive'),
        ('Dead', 'Dead'),
        ('unknown', 'Unknown'),
    )

    STATUS_GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Genderless', 'Genderless'),
        ('unknown', 'Unknown'),
    )

    name = models.CharField(
        'Имя персонжажа',
        max_length=255
    )
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='unknown'
    )
    species = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        blank=True
    )
    gender = models.CharField(
        max_length=255,
        choices=STATUS_GENDER,
        default='unknown'
    )
    origin = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='characters_origin'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='characters_location'
    )
    image = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    created = models.DateTimeField(
        editable=False
    )

    def __str__(self) -> str:
        return self.url


class Location(models.Model):
    '''Локация.'''

    name = models.CharField(
        'Имя локации',
        max_length=255,
        unique=True,
    )
    type = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    created = models.DateTimeField(
        editable=False
    )

    def __str__(self) -> str:
        return self.name


class Episode(models.Model):
    '''Эпизод'''

    name = models.CharField(
        'Имя локации',
        max_length=255,
        unique=True,
    )
    air_date = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)
    characters = models.ManyToManyField(
        Character,
        related_name='episodes'
    )
    url = models.URLField(max_length=255)
    created = models.DateTimeField(
        editable=False
    )

    def __str__(self) -> str:
        return self.url
