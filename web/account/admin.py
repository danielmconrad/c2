from django import forms
from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)
from django.forms import formset_factory
from django.utils.translation import (
    gettext,
    gettext_lazy as _,
)
from .models import (
    User,
    Gender,
    Race,
    Ethnicity,
    UserRaceEthnicity,
)


#
# =================================================
#
# class UserRaceForm(forms.Form):
#     pass
#     # area_skill           = fields.CharField(max_length=50, help_text = 'Example: Testing,Development,etc..')
#     # experience           = fields.CharField(max_length=50)
#
# UserRaceFormset = formset_factory(UserRaceForm, extra=0)

# StackedInline
# TabularInline
class UserRaceEthnicityInline(admin.InlineModelAdmin):
    model = UserRaceEthnicity
    # formset = UserRaceFormset

#
# =================================================
#


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'gender',
        'age',
    )

    readonly_fields = (
        'last_login',
        'username',
        'date_joined',
    )

    inlines = [
        UserRaceEthnicityInline,
    ]

    fieldsets = (
        (
            _('Personal info'),
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender',
                    'date_of_birth',
                    'locations',
                )
            }
        ),
        (
            _('User info'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'username',
                    'password',
                )
            }
        ),
        (
            _('Permissions'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _('Important dates'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    '''Admin View for Gender'''

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
    '''Admin View for Race'''

    list_display = (
        'id',
        'race',
    )
    search_fields = (
        'race',
    )


@admin.register(Ethnicity)
class EthnicityAdmin(admin.ModelAdmin):
    '''Admin View for Ethnicity'''

    list_display = (
        'id',
        'race',
        'ethnicity',
    )

    search_fields = (
        'race',
        'ethnicity',
    )
