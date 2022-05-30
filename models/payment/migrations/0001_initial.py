# Generated by Django 4.0.4 on 2022-05-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_method', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('paid', 'Оплачено'), ('not_paid', 'Не оплачено')], max_length=100, verbose_name='Статус оплаты')),
                ('type', models.JSONField(blank=True, default=dict, null=True)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='payment_method.paymentmethod', verbose_name='Метод оплаты')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
    ]
