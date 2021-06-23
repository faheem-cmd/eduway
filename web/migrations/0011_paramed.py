# Generated by Django 3.2 on 2021-04-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_computer'),
    ]

    operations = [
        migrations.CreateModel(
            name='paramed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('contents', models.URLField(default='')),
                ('phone', models.TextField()),
                ('image', models.ImageField(upload_to='web/engi')),
            ],
            options={
                'verbose_name': 'paramed',
                'verbose_name_plural': 'paramed',
                'db_table': 'web_paramed',
            },
        ),
    ]