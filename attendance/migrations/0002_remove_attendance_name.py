# Generated by Django 2.2.4 on 2020-08-26 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='name',
        ),
    ]
