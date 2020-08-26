from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import SiteUserCreationForm, SiteUserChangeForm, SiteUserAdminCreationForm
from .models import SiteUser


class SiteUserAdmin(UserAdmin):
    add_form = SiteUserCreationForm
    #add_form = SiteUserAdminCreationForm
    form = SiteUserChangeForm
    model = SiteUser
    list_display = ('username','name','gender','email','birthday','date_joined',)
    list_filter = ('gender','name')
    fieldsets = (
        ('Account', {
            'description':'',
            'fields': ('username','password',)
            }
        ),
        ('Info',{
            'fields':('email','name','gender','birthday',)
            }),
        ('Permissions', {
            'classes':('collapse',),
            'fields': ('is_staff', 'is_active'),
            }
        ),
    )

    add_fieldsets = (
        ('Account', {
            'description':'These fields are required.',
            'fields': ('username','password1','password2','email','gender'),
            }
        ),
        ('Info',{
            'description':'Optional fields',
            'fields':('name','birthday')
            }
        ),
    )
    search_fields = ('username','email',)
    ordering = ('username','name',)


admin.site.register(SiteUser, SiteUserAdmin)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)