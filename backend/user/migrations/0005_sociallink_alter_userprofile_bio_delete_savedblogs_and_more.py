# Generated by Django 4.1.3 on 2022-11-19 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_userprofile_bio_userprofile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("url", models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="bio",
            field=models.TextField(blank=True, default="", max_length=500),
        ),
        migrations.DeleteModel(
            name="SavedBlogs",
        ),
        migrations.AddField(
            model_name="sociallink",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]