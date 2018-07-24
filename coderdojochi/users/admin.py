from django import forms
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
    ContactEmail,
    ContactPhone,
    RaceEthnicity,
)


class ContactEmailForm(forms.ModelForm):
    class Meta:
        model = ContactEmail
        exclude = ['user']


class ContactEmailInline(admin.TabularInline):
    classes = ("emails-inline")
    model = ContactEmail
    form = ContactEmailForm


class ContactPhoneForm(forms.ModelForm):
    class Meta:
        model = ContactPhone
        exclude = ['user']


class ContactPhoneInline(admin.TabularInline):
    classes = ['phones-inline']
    model = ContactPhone
    form = ContactPhoneForm


class RaceEthnicityForm(forms.ModelForm):
    class Meta:
        model = RaceEthnicity
        exclude = ['user']

    class Media:
        js = ("user_race_ethnicities_admin.js",)


class RaceEthnicityInline(admin.TabularInline):
    classes = ("user-race-ethnicity-inline",)
    model = RaceEthnicity
    form = RaceEthnicityForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        # 'gender',
        'age',
    )

    readonly_fields = (
        'last_login',
        'username',
        'date_joined',
    )

    inlines = [
        ContactEmailInline,
        ContactPhoneInline,
        RaceEthnicityInline,
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
                    'bio',
                    'date_of_birth',
                    'locations',
                    'schools',
                    'medical_conditions',
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


@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address',
        'active',
    )

    search_fields = (
        'address',
        'active',
    )


@admin.register(ContactPhone)
class ContactPhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'active',
    )

    search_fields = (
        'number',
        'active',
    )
