# Generated by Django 3.2 on 2021-06-06 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_resource_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animation',
            old_name='content',
            new_name='courses',
        ),
        migrations.RenameField(
            model_name='animation',
            old_name='contents',
            new_name='website',
        ),
    ]
