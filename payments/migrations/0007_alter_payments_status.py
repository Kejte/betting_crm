# Generated by Django 5.1.4 on 2025-03-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_payments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='status',
            field=models.CharField(choices=[('WR', 'В работе'), ('AC', 'Принято'), ('CN', 'Отменен')], default='WR', verbose_name='Статус'),
        ),
    ]
