# Generated by Django 2.2.7 on 2019-11-28 01:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rise',
            name='solve',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000, verbose_name='解决裁定'),
            preserve_default=False,
        ),
    ]