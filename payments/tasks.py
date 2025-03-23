from celery import shared_task
from celery.utils.log import get_task_logger
from payments.models import Payments
import datetime

logger = get_task_logger(__name__)


@shared_task
def update_expired_payments():
    Payments.objects.filter(expired_at=datetime.date.today()).update(is_actual=False)