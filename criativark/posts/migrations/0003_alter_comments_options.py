# Generated by Django 4.0.6 on 2022-07-10 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
    ]