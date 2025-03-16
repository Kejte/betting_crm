# Generated by Django 5.1.4 on 2025-03-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_techsupportticket_status_updateticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано?')),
            ],
            options={
                'verbose_name': 'Апдейт лог',
                'verbose_name_plural': 'Апдейт логи',
            },
        ),
    ]
