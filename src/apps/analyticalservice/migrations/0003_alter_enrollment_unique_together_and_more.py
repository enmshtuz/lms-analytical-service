# Generated by Django 5.0.3 on 2024-05-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyticalservice', '0002_badge_news_feedback_subscription_userprofile'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='is_forced_enrollment',
            field=models.BooleanField(default=False),
        ),
    ]