# Generated by Django 3.0 on 2020-01-11 06:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_reference_reference_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
