from django.contrib import admin
from feedback.models import TechSupportTicket, UpdateTicket# UpdateLog

@admin.register(TechSupportTicket)
class TechSupportTicket(admin.ModelAdmin):
    list_display = ('profile', )
    search_fields = ('profile',)

@admin.register(UpdateTicket)
class UpdateTicketAdmin(admin.ModelAdmin):
    list_display = ('profile',)
    search_fields = ('profile',)

# @admin.register(UpdateLog)
# class UpdateLogAdmin(admin.ModelAdmin):
#     list_display = ('created_at',)
