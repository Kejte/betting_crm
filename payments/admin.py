from django.contrib import admin
from payments.models import Tariff

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'cost', 'is_published')
    list_filter=('is_published',)