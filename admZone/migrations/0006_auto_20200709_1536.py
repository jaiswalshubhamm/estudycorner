# Generated by Django 3.0.7 on 2020-07-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admZone', '0005_sms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='msg',
            field=models.TextField(),
        ),
    ]