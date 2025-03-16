from django.db import models
from profiles.models import Profile

class Ticket(models.Model):
    profile = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Тело тикета'
    )

    class Meta:
        abstract = True

class TechSupportTicket(Ticket):
    class TechSupportTicketStatusChoice(models.TextChoices):
        NEW = ('NW', 'Новое')
        IN_WORK = ('WR', 'В работе')
        CLOSED = ('CL', 'Закрыт')

    status = models.CharField(
        verbose_name='Статус',
        choices=TechSupportTicketStatusChoice,
        default=TechSupportTicketStatusChoice.NEW
    )

    def __str__(self):
        return f'Тикет пользователя {self.profile.tg_id}'
    
    class Meta:
        verbose_name='Тикет тех.поддержки'
        verbose_name_plural='Тикеты технической поддержки'

class UpdateTicket(Ticket):
    class UpdateTicketStatusChoice(models.TextChoices):
        NEW = ('NW', 'Новое')
        ACEPTED = ('AC', 'Принято')
    
    status = models.CharField(
        verbose_name='Статус',
        choices=UpdateTicketStatusChoice,
        default=UpdateTicketStatusChoice.NEW
    )

    def __str__(self):
        return f'Предложение пользователя {self.profile.tg_id}'
    
    class Meta:
        verbose_name = 'Тикет на обновление'
        verbose_name_plural = 'Тикеты на обновления'

# class UpdateLog(models.Model):
#     created_at = models.DateTimeField(
#         verbose_name='Дата и время создания',
#         auto_now_add=True
#     )
#     text = models.TextField(
#         verbose_name='Текст'
#     )
#     is_published = models.BooleanField(
#         verbose_name='Опубликовано?',
#         default=False
#     )

#     def __str__(self):
#         return f'Апдейт лог от {self.created_at}'
    
#     class Meta:
#         verbose_name='Апдейт лог'
#         verbose_name_plural='Апдейт логи'
        