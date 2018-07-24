from address.forms import AddressWidget
from address.models import AddressField
from django.contrib import admin

from .models import Location, School


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    '''Admin View for Location'''

    list_display = (
        'address',
        'location_type',
    )

    list_filter = (
        'location_type',
    )

    search_fields = (
        'address',
        'location_type',
    )

    fieldsets = (
        (
            "",
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'address',
                    'location_type',
                )
            }
        ),
    )

    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget(
                attrs={
                    'style': 'width: 400px;'
                }
            )
        }
    }


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    '''Admin View for School'''

    list_display = (
        'id',
        'name',
        'school_type',
    )
    list_filter = (
        'school_type',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )
