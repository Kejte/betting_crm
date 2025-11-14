from django.db import models

class Profile(models.Model):
    tg_id = models.BigIntegerField(
        verbose_name='Телеграм айди',
        unique=True,
        primary_key=True
    )
    username = models.CharField(
        verbose_name='Юзернейм',
        default='@'
    )
    referrer = models.ForeignKey(
        'Profile',
        verbose_name='Реферрер',
        on_delete=models.CASCADE,
        related_name='profile_referrer',
        null=True
    )

    def __str__(self):
        return f'{self.tg_id}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class ReferalProgramAccount(models.Model):
    profile = models.OneToOneField(
        Profile,
        verbose_name='Реферрер',
        on_delete=models.CASCADE
    )
    balance = models.BigIntegerField(
        verbose_name='Баланс партнерской программы',
        default=0
    )
    referal_count = models.BigIntegerField(
        verbose_name='Количество рефераллов',
        default=0
    )
    total_earnings = models.BigIntegerField(
        verbose_name='Всего заработано',
        default=0
    )
    referal_url = models.CharField(
        verbose_name='Реферальная ссылка',
        unique=True,
        default=''
    )

    def __str__(self):
        return f'Аккаунт реферальной системы {self.profile.username}({self.profile.pk})'
    
    class Meta:
        verbose_name = 'Аккаунт реферальной программы'
        verbose_name_plural = 'Аккаунты реферальной программы'

class FreebetFilter(models.Model):
    slug = models.CharField(
        verbose_name='Букмекеры'
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Создатель фильтра'
    )
    surebet_url = models.TextField(
        verbose_name='Ссылка на surebet',
        null=True
    )
    excluded_bookers = models.JSONField(
        verbose_name='Исключенные конторы',
        default=dict,
        null=True
    )

    def __str__(self):
        return f'Фильтр {self.profile.pk} для {self.slug}'
    
    class Meta:
        verbose_name = 'Фильтр для фрибетов'
        verbose_name_plural = 'Фильтры для фрибетов'

class BookmakerFilterModel(models.Model):
    slug = models.CharField(
        verbose_name='Букмекеры'
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Создатель фильтра'
    )
    name = models.CharField(
        verbose_name='Название'
    )
    surebet_url = models.TextField(
        verbose_name='Ссылка на surebet',
        null=True
    )
    excluded_bookers = models.JSONField(
        verbose_name='Исключенные конторы',
        default=dict,
        null=True
    )
    max_coef_first_book = models.FloatField(
        verbose_name='Максималньый коэффициент первая бк',
        null=True
    )
    min_coef_first_book = models.FloatField(
        verbose_name='Минимальный коэффициент первая бк',
        null=True
    )
    max_coef_second_book = models.FloatField(
        verbose_name='Максималньый коэффициент вторая бк',
        null=True
    )
    min_coef_second_book = models.FloatField(
        verbose_name='Минимальный коэффициент вторая бк',
        null=True
    )

    def __str__(self):
        return f'Фильтр {self.profile.pk} для {self.slug}'
    
    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтр'