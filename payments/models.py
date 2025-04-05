from django.db import models
from profiles.models import Profile

def upload_to_tariff_photo(instance,filename):
    return f'tariffs/{instance.title}/{filename}'

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
    photo = models.ImageField(
        verbose_name='Превью тарифа',
        upload_to=upload_to_tariff_photo,
        null=True
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
        CANCELED = ('CN', 'Отменен')
        

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
    promocode = models.ForeignKey(
        'Promocode',
        on_delete=models.SET_NULL,
        null=True,
        related_name='payment_promocode',
        blank=True
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

class Promocode(models.Model):
    promo = models.CharField(
        verbose_name='Промокод',
        max_length=10
    )
    tariff = models.ForeignKey(
        Tariff,
        verbose_name='Тарифф',
        on_delete=models.CASCADE,
        related_name='tariff_promocodes'
    )
    remained = models.IntegerField(
        verbose_name='Осталось использований'
    )
    discount = models.IntegerField(
        verbose_name='Скидка',
        help_text='руб.'
    )
    is_active = models.BooleanField(
        verbose_name='Активно?',
        default=False
    )

    def __str__(self):
        return f'Промокод тарифа {self.tariff.title}'
    
    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

class ActivatedPromocode(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    promocode = models.ForeignKey(
        Promocode,
        on_delete=models.CASCADE,
    )
    buyed = models.BooleanField(
        verbose_name='Купили?',
        default=False
    ) 