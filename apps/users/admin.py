from django.contrib import admin
from django.contrib.auth.models import User

from apps.users.models import Position


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'position', 'is_active')
    search_fields = ('username', 'email', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
