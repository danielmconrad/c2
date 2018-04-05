from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)
from django.utils.translation import (
    gettext,
    gettext_lazy as _,
)
from .models import (
    User,
    RaceEthnicity,
    Gender,
)


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
                    'address',
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


@admin.register(RaceEthnicity)
class RaceEthnicityAdmin(admin.ModelAdmin):
    '''Admin View for RaceEthnicity'''

    list_display = (
        'id',
        'race_ethnicity',
    )
    search_fields = (
        'race_ethnicity',
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
