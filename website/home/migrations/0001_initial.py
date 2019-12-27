# Generated by Django 3.0.1 on 2019-12-27 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('post_description', models.TextField()),
                ('post_status', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]