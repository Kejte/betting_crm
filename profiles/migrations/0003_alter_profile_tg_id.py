# Generated by Django 5.1.4 on 2025-03-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tg_id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Телеграм айди'),
        ),
    ]
