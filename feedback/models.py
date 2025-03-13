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

    def __str__(self):
        return f'Тикет пользователя {self.profile.tg_id}'
    
    class Meta:
        verbose_name='Тикет тех.поддержки'
        verbose_name_plural='Тикеты технической поддержки'

class UpdateTicket(Ticket):
    class UpdateTicketStatusChoice(models.TextChoices):
        NEW = ('NW', 'Новое')
        IN_WORK = ('WR', 'На рассмотрении')
        VOTE = ('VT', 'Голосование')
        ACEPTED = ('AC', 'Принято')
        CANCELED = ('CN', 'Отклонено')
    
    def __str__(self):
        return f'Предложение пользователя {self.profile.tg_id}'
    
    class Meta:
        verbose_name = 'Тикет на обновление'
        verbose_name_plural = 'Тикеты на обновления'
        