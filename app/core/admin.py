from django.contrib import admin
from core.models import User,Recipe,Tag
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _ ## To implemet transaltions
# Register your models here.


class UserAdmin(BaseUserAdmin):
    """Define the admin page for users"""
    ordering = ['id']
    list_display = ['email','name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']

    #THis is for adding Users in the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )





admin.site.register(User,UserAdmin)
admin.site.register(Recipe)
admin.site.register(Tag)