# Generated by Django 3.2.3 on 2021-05-27 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myWebpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='mail',
            new_name='email',
        ),
    ]
