# Generated by Django 4.0.4 on 2022-05-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
