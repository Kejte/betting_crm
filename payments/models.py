from django.db import models
from profiles.models import Profile

class Tariff(models.Model):
    title = models.CharField(
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    cost = models.IntegerField(
        verbose_name='Стоимость',
        help_text='Руб./мес'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано?',
        default=False
    )
    duration = models.IntegerField(
        verbose_name='Продолжительность',
        help_text='Дней',
        default=30
    )

    def __str__(self):
        return f'Тариф {self.title}'
    
    class Meta:
        verbose_name='Тариф'
        verbose_name_plural='Тарифы'

class Subscription(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True,
        related_name='profile_subscription'
    )
    
    def __str__(self):
        return f'Подписка пользователя {self.profile.username}'

    class Meta:
        verbose_name='Подписка'
        verbose_name_plural = 'Подписки'

class Payments(models.Model):
    class PaymentStatusChoice(models.TextChoices):
        IN_WORK = ('WR', 'В работе')
        ACCEPTED = ('AC', 'Принято')
        

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Связь с подпиской',
        related_name='subscription_payments'
    )
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.PROTECT,
        verbose_name='Тариф'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    expired_at = models.DateField(
        verbose_name='Дата истечения',
    )
    is_actual = models.BooleanField(
        verbose_name='Актуально?',
        default=False
    )
    status = models.CharField(
        verbose_name='Статус',
        choices=PaymentStatusChoice,
        default=PaymentStatusChoice.IN_WORK
    )
    
    @property
    def cost(self):
        return self.tariff.cost
    
    def __str__(self):
        return f'Платеж пользователя {self.subscription.profile.username}'

    class Meta:
        verbose_name='Платёж'
        verbose_name_plural='Платежи'

class ActivatedTrialPeriod(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Профиль',
    )
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.CASCADE,
        verbose_name='Тарифф'
    )

    def __str__(self):
        return f'Пробный период тарифа {self.tariff.title} пользователя {self.profile.username}'
    
    class Meta:
        verbose_name = 'Пробный период'
        verbose_name_plural = 'Пробные периоды'