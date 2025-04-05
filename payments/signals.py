from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from payments.models import Payments, Promocode, ActivatedPromocode

@receiver(post_save, sender=Payments)
def update_payments(sender: type[Payments], instance: Payments, created: bool, **kwargs):
    if instance.is_actual:
        Payments.objects.filter(subscription=instance.subscription).exclude(pk=instance.pk).update(is_actual=False)

@receiver(post_save, sender=Promocode)
def update_promocode(sender: type[Promocode], instance: Promocode, **kwargs):
    if instance.remained == 0:
        instance.is_active = False
        instance.save()
        ActivatedPromocode.objects.filter(promo__pk=instance.pk).delete()