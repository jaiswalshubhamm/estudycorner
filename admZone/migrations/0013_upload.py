# Generated by Django 3.0.7 on 2020-07-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admZone', '0012_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('fname', models.TextField()),
                ('dt', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'upload',
            },
        ),
    ]