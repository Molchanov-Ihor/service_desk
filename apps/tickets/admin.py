from django.contrib import admin

from apps.tickets.models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'executor', 'status', 'created_at')
    search_fields = ('title',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
