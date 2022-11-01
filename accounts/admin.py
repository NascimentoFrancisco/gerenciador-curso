from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    list_display = ('cpf', 'is_superuser','is_staff', 'is_active',)
    list_filter = ('cpf', 'is_superuser','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'password1', 'password2', 'is_superuser','is_staff', 'is_active')}
        ),
    )
    search_fields = ('cpf',)
    ordering = ('cpf',)

admin.site.register(CustomUser, CustomUserAdmin)
