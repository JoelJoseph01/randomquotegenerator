# Generated by Django 3.0.7 on 2020-06-29 04:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('randq', '0002_auto_20200629_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='qu',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
