# Generated by Django 3.0.7 on 2020-06-29 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randq', '0003_qu_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qu',
            name='title',
        ),
    ]
