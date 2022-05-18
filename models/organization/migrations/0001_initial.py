# Generated by Django 4.0.4 on 2022-05-18 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование организации')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Адрес организации')),
                ('RNN', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{12,12}$')])),
                ('BIN', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{12,12}$')])),
                ('bank_requisition', models.CharField(max_length=100, verbose_name='Реквизиты банка')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
