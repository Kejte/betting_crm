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

    def __str__(self):
        return f'Тариф {self.title}'
    
    class Meta:
        verbose_name='Тариф'
        verbose_name_plural='Тарифы'