# Generated by Django 3.1.2 on 2020-12-27 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0011_auto_20201227_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='frequency',
        ),
    ]
