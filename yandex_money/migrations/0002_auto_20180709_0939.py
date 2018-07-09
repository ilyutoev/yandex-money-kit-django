# Generated by Django 2.0.6 on 2018-07-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fail_url',
            field=models.URLField(default='https://example.com/fail-payment/', verbose_name='URL неуспешной оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='scid',
            field=models.PositiveIntegerField(default=12345, verbose_name='Номер витрины'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shop_id',
            field=models.PositiveIntegerField(default=56789, verbose_name='ID магазина'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='success_url',
            field=models.URLField(default='https://example.com/success-payment/', verbose_name='URL успешной оплаты'),
        ),
    ]
