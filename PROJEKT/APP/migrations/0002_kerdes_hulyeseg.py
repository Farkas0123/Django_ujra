# Generated by Django 3.2.12 on 2022-03-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kerdes',
            name='hulyeseg',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
