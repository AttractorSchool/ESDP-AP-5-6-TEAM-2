# Generated by Django 4.0.4 on 2022-06-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]