# Generated by Django 3.2 on 2021-04-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_title_med_titles'),
    ]

    operations = [
        migrations.CreateModel(
            name='arts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('contents', models.URLField(default='')),
                ('image', models.ImageField(upload_to='web/arts')),
            ],
            options={
                'verbose_name': 'arts',
                'verbose_name_plural': 'arts',
                'db_table': 'web_arts',
            },
        ),
    ]