# Generated by Django 4.0 on 2021-12-28 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='phone_name',
            field=models.CharField(max_length=120),
        ),
    ]