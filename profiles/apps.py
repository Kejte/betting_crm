from django.apps import AppConfig
from django.core.signals import setting_changed

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    verbose_name = 'Управление профилями'

    def ready(self):
        from .signals import update_referal_program_account

        setting_changed.connect(update_referal_program_account)
        return super().ready()