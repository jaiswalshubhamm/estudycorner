# Generated by Django 3.0.7 on 2020-07-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admZone', '0003_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('txt', models.TextField(default='')),
                ('dt', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'email',
            },
        ),
    ]
