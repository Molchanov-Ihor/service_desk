from django.contrib import admin

from apps.users.models import Position, CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'position', 'is_active')
    search_fields = ('username', 'email', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
