# Generated by Django 5.1.4 on 2025-03-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_subscription_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='expired_at',
            field=models.DateField(verbose_name='Дата истечения'),
        ),
    ]
