# Generated by Django 3.2 on 2021-05-05 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_songs_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='music',
        ),
    ]
