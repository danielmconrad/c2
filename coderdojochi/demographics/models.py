from django.db import models


class Gender(models.Model):
    """Model definition for Gender."""

    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    REFERRED_AS_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
    )

    gender = models.CharField(
        max_length=255
    )

    referred_to_as = models.CharField(
        max_length=1,
        choices=REFERRED_AS_CHOICES,
        default=FEMALE,
    )

    class Meta:
        """Meta definition for Gender."""
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        """Unicode representation of Gender."""
        return f"{self.gender}"


class Race(models.Model):
    """Model definition for Race."""

    race = models.CharField(
        max_length=255
    )

    class Meta:
        """Meta definition for Race."""
        verbose_name = 'Race'
        verbose_name_plural = 'Races'

    def __str__(self):
        """Unicode representation of Race."""
        return f"{self.race}"


class Ethnicity(models.Model):
    """Model definition for Ethnicity."""

    ethnicity = models.CharField(
        max_length=255
    )

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for Ethnicity."""
        verbose_name = 'Ethnicity'
        verbose_name_plural = 'Ethnicities'

    def __str__(self):
        """Unicode representation of Ethnicity."""
        return f"{self.race}: {self.ethnicity}"
