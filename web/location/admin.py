from django.contrib import admin

from address.forms import AddressWidget
from address.models import AddressField

from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    '''Admin View for Location'''

    list_display = (
        'address',
        'type',
    )

    list_filter = (
        'type',
    )

    search_fields = (
        'address',
        'type',
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
                    'type',
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
