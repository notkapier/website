# Generated by Django 3.0 on 2019-12-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20191229_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='poststatus',
            new_name='status',
        ),
    ]
