# Generated by Django 3.0.6 on 2020-05-11 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0008_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='remark',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
