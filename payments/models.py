from django.db import models

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
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    