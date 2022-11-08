# Generated by Django 4.1.3 on 2022-11-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='summary',
            field=models.TextField(blank=True, default=''),
        ),
    ]
