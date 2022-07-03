from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Hashed_code, NewUser
from .models import *


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'is_doctor', 'full_name')
    list_filter = ('is_doctor', 'full_name', 'is_staff',
                   'is_superuser', 'is_active')
    ordering = ('email', 'user_name', 'is_doctor', 'full_name')
    list_display = ('email', 'user_name','img' ,'is_doctor',
                    'full_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('user_name','img', 'is_doctor', 'full_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'user_name','img', 'is_doctor', 'full_name', 'password1', 'password2')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Formulaire)


