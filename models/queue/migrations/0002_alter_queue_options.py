# Generated by Django 4.0.4 on 2022-06-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='queue',
            options={'verbose_name': 'Очередь', 'verbose_name_plural': 'Очередь'},
        ),
    ]