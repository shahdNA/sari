# Generated by Django 4.0.4 on 2022-05-24 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_city_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
    ]
