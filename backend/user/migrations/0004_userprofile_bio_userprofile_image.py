# Generated by Django 4.1.3 on 2022-11-19 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_savedblogs_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="bio",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(blank=True, upload_to="profile_image"),
        ),
    ]
