# Generated by Django 3.2.4 on 2021-06-26 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centres', '0004_auto_20210626_0520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcentre',
            old_name='street_address',
            new_name='address',
        ),
    ]
