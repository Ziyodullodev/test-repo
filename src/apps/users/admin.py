from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'full_name', 'email', 'telegram_id')

    search_fields = ('username', 'first_name', 'last_name', 'email', 'telegram_id')

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
        'first_name', 'last_name', 'email', 'telegram_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    ordering = ('username',)

    readonly_fields = ('date_joined', 'last_login')


admin.site.register(User, UserAdmin)
