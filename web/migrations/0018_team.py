# Generated by Django 3.2 on 2021-05-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_agri'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('position', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='web/engi')),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'team',
                'db_table': 'web_team',
            },
        ),
    ]
