import uuid

from django.contrib.auth.models import UserManager as DefaultUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.utils import timezone

from location.models import Location


class UserManager(DefaultUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        super().create_user(username=uuid.uuid4(), email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        super().create_superuser(username=uuid.uuid4(), email=email, password=password, **extra_fields)


class User(AbstractUser):
    """
    Stores a single user, related to :model:`account.Gender`.
    """

    objects = UserManager()

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )

    gender = models.ForeignKey(
        'Gender',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    races = models.ManyToManyField(
        'Race',
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    addresses = models.ManyToManyField(
        Location,
        limit_choices_to=(
            Q(location_type=Location.HOME) | Q(location_type=Location.WORK)
        ),
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def age(self, date=timezone.now()):
        """
        Returns the age of the User in number of years.
        Uses current date if `date` not passed.
        """

        if self.date_of_birth is None:
            return None

        return date.year - self.date_of_birth.year - (
            (date.month, date.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
    age.short_description = 'Age'


class Race(models.Model):
    """Model definition for Race."""

    race = models.CharField(
        max_length=255
    )

    class Meta:
        """Meta definition for RaceEthnicity."""
        verbose_name = 'Race'
        verbose_name_plural = 'Races'

    def __str__(self):
        """Unicode representation of Race."""
        return self.race


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
        return self.ethnicity


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
        return self.gender
