# Generated by Django 3.0.1 on 2019-12-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_location',
            field=models.ImageField(null='TRUE', upload_to='uploads/'),
            preserve_default='TRUE',
        ),
    ]
