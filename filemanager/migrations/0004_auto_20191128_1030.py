# Generated by Django 2.2.7 on 2019-11-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0003_auto_20191121_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]