from django.db import models

class Profile(models.Model):
    tg_id = models.IntegerField(
        verbose_name='Телеграм айди',
        unique=True,
        primary_key=True
    )

    def __str__(self):
        return f'{self.tg_id}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
