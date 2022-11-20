# Generated by Django 4.1.3 on 2022-11-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_tag_blogpost_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogpost",
            options={"ordering": ["-created_at"]},
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="tags",
        ),
        migrations.AddField(
            model_name="tag",
            name="blogpost",
            field=models.ManyToManyField(related_name="tags", to="blog.blogpost"),
        ),
    ]