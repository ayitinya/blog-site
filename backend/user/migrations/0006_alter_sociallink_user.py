# Generated by Django 4.1.3 on 2022-11-19 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_sociallink_alter_userprofile_bio_delete_savedblogs_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sociallink",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
