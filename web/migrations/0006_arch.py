# Generated by Django 3.2 on 2021-04-19 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_comm_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='arch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('contents', models.URLField(default='')),
                ('phone', models.TextField()),
                ('image', models.ImageField(upload_to='web/engi')),
            ],
            options={
                'verbose_name': 'arch',
                'verbose_name_plural': 'arch',
                'db_table': 'web_arch',
            },
        ),
    ]
