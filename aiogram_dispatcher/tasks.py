from celery import shared_task
from celery.utils.log import get_task_logger
from aiogram_dispatcher.triggers import send_fokrs_to_private_group, send_live_forks


logger = get_task_logger(__name__)


@shared_task
def triggered_send_fokrs_to_private_group():
    send_fokrs_to_private_group()
    logger.info('Triggered send_forks_to_private_group')

@shared_task
def triggered_send_live_forks_to_private_group():
    send_live_forks()
    logger.info('Triggered send_live_forks')