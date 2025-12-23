from django.contrib import admin

from apps.tickets.models import Ticket, Status


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'executor', 'status', 'created_at')
    search_fields = ('title',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
