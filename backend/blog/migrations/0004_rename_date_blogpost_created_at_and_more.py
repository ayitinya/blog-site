# Generated by Django 4.1.3 on 2022-11-07 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blogpost_subtitle_alter_blogpost_body_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost",
            old_name="date",
            new_name="created_at",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="summary",
        ),
    ]