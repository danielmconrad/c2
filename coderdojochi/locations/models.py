from address.models import AddressField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Location(models.Model):
    """Model definition for Location."""

    SCHOOL = 'S'
    CLASS = 'C'
    HOME = 'H'
    WORK = 'W'
    TYPE_CHOICES = (
        (SCHOOL, 'School'),
        (CLASS, 'Class'),
        (HOME, 'Home'),
        (WORK, 'Work'),
    )

    address = AddressField(
        on_delete=models.CASCADE,
    )

    location_type = models.CharField(
        db_column="type",
        choices=TYPE_CHOICES,
        default=HOME,
        max_length=1,
    )

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """Unicode representation of Location."""
        location_type = dict(self.TYPE_CHOICES).get(self.location_type)
        return f'({location_type}) {self.address}'


class School(models.Model):
    """Model definition for School."""

    BOARDING = 'B'
    CHARTER = 'C'
    HOMESCHOOL = 'H'
    LANGUAGE_IMMERSION = 'LI'
    MAGNET = 'M'
    MONTESSORI = 'MO'
    ONLINE = 'O'
    PAROCHIAL = 'PA'
    PRIVATE = 'PR'
    PRIVATE_SPECIAL_EDUCATION = 'PS'
    PUBLIC = 'P'
    REGGIO_EMILIA = 'RE'
    RELIGIOUS = 'R'
    WALDORF = 'W'

    SCHOOL_TYPE_CHOICES = (
        (BOARDING, 'Boarding'),
        (CHARTER, 'Charter'),
        (HOMESCHOOL, 'Homeschool'),
        (LANGUAGE_IMMERSION, 'Language Immersion'),
        (MAGNET, 'Magnet'),
        (MONTESSORI, 'Montessori'),
        (ONLINE, 'Online'),
        (PAROCHIAL, 'Parochial'),
        (PRIVATE_SPECIAL_EDUCATION, 'Private Special Education'),
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
        (REGGIO_EMILIA, 'Reggio Emilia'),
        (RELIGIOUS, 'Religious'),
        (WALDORF, 'Waldorf'),
    )

    name = models.CharField(
        max_length=200,
    )

    address = models.ForeignKey(
        'Location',
        limit_choices_to={
            'location_type': Location.SCHOOL
        },
        on_delete=models.CASCADE,
    )

    school_type = models.CharField(
        db_column="type",
        choices=SCHOOL_TYPE_CHOICES,
        default=PUBLIC,
        max_length=2,
    )

    phone_number = PhoneNumberField(
        null=True,
        blank=True,
    )

    website = models.URLField(
        null=True,
        blank=True,
        max_length=200,
    )

    class Meta:
        """Meta definition for School."""

        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        """Unicode representation of School."""
        return f"{self.name}"
