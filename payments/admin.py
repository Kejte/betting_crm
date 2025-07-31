from django.contrib import admin
from payments.models import Tariff, Subscription, Payments, Promocode, ActivatedPromocode
from django.contrib.admin import SimpleListFilter
from django.db.models import Case, When, BooleanField

class SubscriptionFilter(SimpleListFilter):
    title = 'С активной подпиской' # or use _('country') for translated title
    parameter_name = 'С активной подпиской'
    

    def lookups(self, request, model_admin):
        return [('С активной подпиской','С активной подпиской')]

    def queryset(self, request, queryset):
        if self.value() == 'С активной подпиской':
            return queryset.annotate(active_sub=Case(
                When(subscription_payments__is_actual=True, then=True),
                default=False,
                output_field=BooleanField()
            )).filter(active_sub=True)

class PromocodeInline(admin.TabularInline):
    model = Promocode
    extra = 1

@admin.register(ActivatedPromocode)
class ActivatedPromocodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'cost', 'is_published')
    list_filter=('is_published',)
    inlines = (PromocodeInline,)

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
    list_filter = (SubscriptionFilter,)
    autocomplete_fields = ('profile',)