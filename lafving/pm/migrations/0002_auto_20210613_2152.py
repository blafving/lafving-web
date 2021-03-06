# Generated by Django 3.2.4 on 2021-06-14 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='session',
            name='start',
            field=models.TimeField(default=datetime.datetime(2021, 6, 13, 21, 52), help_text='Hit Save and Continue Editing. Then hit save when done to stop the session.'),
        ),
    ]
