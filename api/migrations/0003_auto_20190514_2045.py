# Generated by Django 2.2 on 2019-05-14 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190513_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 20, 45, 12, 117028)),
        ),
    ]