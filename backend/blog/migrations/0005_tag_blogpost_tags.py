# Generated by Django 4.1.3 on 2022-11-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_date_blogpost_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
            ],
        ),
        migrations.AddField(
            model_name="blogpost",
            name="tags",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]
