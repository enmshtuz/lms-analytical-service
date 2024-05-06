# Generated by Django 5.0.3 on 2024-05-05 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_quiz_deadline_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='success_criteria',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(101)]),
        ),
    ]