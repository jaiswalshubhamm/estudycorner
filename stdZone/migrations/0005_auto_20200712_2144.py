# Generated by Django 3.0.7 on 2020-07-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stdZone', '0004_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='answer',
        ),
    ]
