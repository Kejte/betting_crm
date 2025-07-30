from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from payments.models import Payments, Promocode, ActivatedPromocode
from aiogram_dispatcher.triggers import give_trial_sub

@receiver(post_save, sender=Payments)
def update_payments(sender: type[Payments], instance: Payments, created: bool, **kwargs):
    if instance.is_actual:
        Payments.objects.filter(subscription=instance.subscription).exclude(pk=instance.pk).update(is_actual=False)
    if instance.trial:
        give_trial_sub(instance.subscription.profile.pk)

@receiver(post_save, sender=Promocode)
def update_promocode(sender: type[Promocode], instance: Promocode, **kwargs):
    if instance.remained == 0:
        instance.is_active = False
        instance.save()
        ActivatedPromocode.objects.filter(promo__pk=instance.pk).delete()