# Generated by Django 3.0 on 2019-12-28 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191228_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_name', models.CharField(max_length=300)),
                ('element_description', models.TextField()),
                ('element_image', models.ImageField(null='TRUE', upload_to='uploads/')),
                ('element_attachment', models.FileField(null='TRUE', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Traccer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traccer_type', models.CharField(max_length=300)),
                ('traccer_image', models.ImageField(null='TRUE', upload_to='uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='reference',
            name='reference_attachment',
            field=models.FileField(null='TRUE', upload_to='uploads'),
            preserve_default='TRUE',
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='TraccerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traccer_item_title', models.CharField(max_length=300)),
                ('traccer_item_description', models.TextField()),
                ('traccer_item_image', models.ImageField(null='TRUE', upload_to='uploads/')),
                ('traccer_item_attachment', models.FileField(null='TRUE', upload_to='uploads/')),
                ('traccer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Traccer')),
            ],
        ),
    ]
