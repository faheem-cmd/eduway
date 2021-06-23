# Generated by Django 3.2 on 2021-05-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_pharma'),
    ]

    operations = [
        migrations.CreateModel(
            name='veti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('contents', models.URLField(default='')),
                ('phone', models.TextField()),
                ('image', models.ImageField(upload_to='web/engi')),
            ],
            options={
                'verbose_name': 'veti',
                'verbose_name_plural': 'veti',
                'db_table': 'web_veti',
            },
        ),
    ]