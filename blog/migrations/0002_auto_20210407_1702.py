# Generated by Django 3.1.7 on 2021-04-07 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date_created',
            new_name='Date Created',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='Title',
        ),
    ]