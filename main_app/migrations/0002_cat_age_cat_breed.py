# Generated by Django 5.0.7 on 2024-07-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cat',
            name='breed',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
