from django.contrib import admin
from payments.models import Tariff, Subscription, Payments

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'cost', 'is_published')
    list_filter=('is_published',)

class PaymentsInline(admin.TabularInline):
    model = Payments
    extra = 1
    readonly_fields = ('_cost',)

    def _cost(self, obj: Payments):
        return obj.tariff.cost

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('profile',)
    search_fields = ('profile__username',)
    inlines = (PaymentsInline,)