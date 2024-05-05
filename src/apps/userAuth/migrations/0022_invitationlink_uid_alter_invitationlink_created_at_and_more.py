# Generated by Django 5.0.3 on 2024-05-03 14:46

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0021_invitationlink_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationlink',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='invitationlink',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='invitationlink',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
