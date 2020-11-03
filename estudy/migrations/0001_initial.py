# Generated by Django 3.0.7 on 2020-07-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=8)),
                ('dob', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('mobno', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('picture', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]