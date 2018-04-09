from django.db import models

from address.models import AddressField


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

    type = models.CharField(
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
        type = dict(self.TYPE_CHOICES).get(self.type)
        return f'({type}) {self.address}'
