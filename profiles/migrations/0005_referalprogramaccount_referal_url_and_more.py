# Generated by Django 5.1.4 on 2025-04-12 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_referrer_referalprogramaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='referalprogramaccount',
            name='referal_url',
            field=models.CharField(default='', unique=True, verbose_name='Реферальная ссылка'),
        ),
        migrations.AlterField(
            model_name='referalprogramaccount',
            name='balance',
            field=models.BigIntegerField(default=0, verbose_name='Баланс партнерской программы'),
        ),
        migrations.AlterField(
            model_name='referalprogramaccount',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', verbose_name='Реферрер'),
        ),
        migrations.AlterField(
            model_name='referalprogramaccount',
            name='referal_count',
            field=models.BigIntegerField(default=0, verbose_name='Количество рефераллов'),
        ),
        migrations.AlterField(
            model_name='referalprogramaccount',
            name='total_earnings',
            field=models.BigIntegerField(default=0, verbose_name='Всего заработано'),
        ),
    ]
