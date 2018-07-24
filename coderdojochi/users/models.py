import uuid

from django.contrib.auth.models import UserManager as DefaultUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.utils import timezone

from coderdojochi.locations.models import Location, School
from coderdojochi.demographics.models import Gender, Race, Ethnicity

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(DefaultUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        super().create_user(
            username=uuid.uuid4(),
            email=email,
            password=password,
            **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        super().create_superuser(
            username=uuid.uuid4(),
            email=email,
            password=password,
            **extra_fields
        )


class User(AbstractUser):
    """
    Stores a single user, related to :model:`users.Gender`.
    """

    objects = UserManager()

    bio = models.TextField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )

    gender = models.ForeignKey(
        Gender,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    locations = models.ManyToManyField(
        Location,
        blank=True,
        limit_choices_to=(
            Q(location_type=Location.HOME) | Q(location_type=Location.WORK)
        ),
    )

    medical_conditions = models.TextField(
        null=True,
        blank=True,
    )

    schools = models.ManyToManyField(
        School,
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


class ContactEmail(models.Model):
    """Model for simple email storage"""

    active = models.BooleanField(
        default=True,
    )

    address = models.EmailField()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_emails',
    )

    class Meta:
        """Meta definition for ContactEmail."""

        verbose_name = 'Contact Email'
        verbose_name_plural = 'Contact Emails'

    def __str__(self):
        """Unicode representation of Contact Email."""
        return self.address


class ContactPhone(models.Model):
    """Model for simple Phone storage"""

    active = models.BooleanField(
        default=True,
    )

    number = PhoneNumberField(
        help_text="Please use the following format: <em>+1 XXX-XXX-XXXX</em>",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_phones',
    )

    class Meta:
        """Meta definition for Phone."""

        verbose_name = 'Contact Phone'
        verbose_name_plural = 'Contact Phones'

    def __str__(self):
        """Unicode representation of ContactPhone."""
        return f"{self.number}"


class RaceEthnicity(models.Model):
    """Model definition for RaceEthnicity."""

    ethnicity = models.ForeignKey(
        Ethnicity,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    other = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )

    race = models.ForeignKey(
        Race,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for RaceEthnicity."""
        verbose_name = 'RaceEthnicity'
        verbose_name_plural = 'RaceEthnicities'

    def __str__(self):
        """Unicode representation of RaceEthnicity."""
        return f"{self.race} {self.ethnicity} {self.other}"
