# Generated by Django 3.0 on 2020-01-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200102_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='traccer',
            options={'verbose_name_plural': 'Traccers'},
        ),
        migrations.AddField(
            model_name='reference',
            name='pub_date',
            field=models.DateTimeField(null='TRUE', verbose_name='date published'),
            preserve_default='TRUE',
        ),
    ]
