# Generated by Django 3.1.2 on 2020-12-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0005_contact_topnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='bnews',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='snews',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='wnews',
            field=models.BooleanField(default=False),
        ),
    ]