# Generated by Django 3.2 on 2021-04-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20210428_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('contents', models.URLField(default='')),
                ('phone', models.TextField()),
                ('image', models.ImageField(upload_to='web/engi')),
            ],
            options={
                'verbose_name': 'computer',
                'verbose_name_plural': 'computer',
                'db_table': 'web_computer',
            },
        ),
    ]