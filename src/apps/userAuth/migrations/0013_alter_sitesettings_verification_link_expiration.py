# Generated by Django 5.0.3 on 2024-04-28 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0012_alter_sitesettings_verification_link_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='verification_link_expiration',
            field=models.DurationField(default=datetime.timedelta(seconds=18000)),
        ),
    ]