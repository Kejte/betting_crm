from django.apps import AppConfig
from django.core.signals import setting_changed



class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'
    verbose_name = 'Платежи'

    def ready(self):
        from .signals import update_payments, update_promocode

        setting_changed.connect(update_payments)
        setting_changed.connect(update_promocode)
        return super().ready()