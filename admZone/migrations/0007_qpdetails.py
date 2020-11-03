# Generated by Django 3.0.7 on 2020-07-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admZone', '0006_auto_20200709_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='QPDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('tq', models.CharField(max_length=5)),
                ('udt', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'qpdetails',
            },
        ),
    ]