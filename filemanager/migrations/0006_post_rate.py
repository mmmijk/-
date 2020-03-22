# Generated by Django 2.2.7 on 2019-12-21 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0005_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.OneToOneField(default=4.0, on_delete=django.db.models.deletion.CASCADE, to='filemanager.Rate', verbose_name='得分'),
            preserve_default=False,
        ),
    ]
