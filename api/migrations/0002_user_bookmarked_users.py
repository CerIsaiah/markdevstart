# Generated by Django 5.0.7 on 2024-08-01 01:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bookmarked_users",
            field=models.ManyToManyField(
                related_name="bookmarked_by", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]