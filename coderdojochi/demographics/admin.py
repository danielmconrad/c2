from django.contrib import admin

from .models import (
    Gender,
    Race,
    Ethnicity,
)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'gender',
        'referred_to_as',
    )
    search_fields = (
        'gender',
        'referred_to_as',
    )


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'race',
    )
    search_fields = (
        'race',
    )


@admin.register(Ethnicity)
class EthnicityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'race',
        'ethnicity',
    )

    search_fields = (
        'race',
        'ethnicity',
    )
