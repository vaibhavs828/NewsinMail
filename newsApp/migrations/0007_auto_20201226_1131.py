# Generated by Django 3.1.2 on 2020-12-26 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0006_auto_20201226_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='bnews',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='snews',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='wnews',
        ),
    ]