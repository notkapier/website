# Generated by Django 3.0 on 2020-01-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_course_course_abv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_abv',
            field=models.CharField(max_length=10),
        ),
    ]
