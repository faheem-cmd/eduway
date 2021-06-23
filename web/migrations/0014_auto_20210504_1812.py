# Generated by Django 3.2 on 2021-05-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_admisiion_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='aviation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('contents', models.URLField(default='')),
                ('phone', models.TextField()),
                ('image', models.ImageField(upload_to='web/engi')),
            ],
            options={
                'verbose_name': 'aviation',
                'verbose_name_plural': 'aviation',
                'db_table': 'web_aviation',
            },
        ),
        migrations.DeleteModel(
            name='admisiion',
        ),
        migrations.DeleteModel(
            name='search',
        ),
    ]
