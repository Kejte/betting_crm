from celery import shared_task
from celery.utils.log import get_task_logger
from payments.models import Payments, ObservedTopicSettings
import datetime
from aiogram_dispatcher.tasks import triger_notify_expired_private_sub

logger = get_task_logger(__name__)


@shared_task
def update_expired_payments():
    payments = Payments.objects.filter(expired_at=datetime.date.today())
    private_payments = list(payments.filter(tariff__is_private=True).values('subscription__profile__tg_id', 'subscription__profile__username'))
    payments.update(is_actual=False)
    if len(private_payments) != 0:
        triger_notify_expired_private_sub.delay(private_payments)
        for private_payment in private_payments:
            ObservedTopicSettings.objects.filter(profile__tg_id=private_payment['subscription__profile__tg_id']).update(is_active=False)