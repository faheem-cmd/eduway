# Generated by Django 3.2 on 2021-06-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_veti'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contact',
                'db_table': 'web_contact',
            },
        ),
    ]
