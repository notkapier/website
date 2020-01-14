# Generated by Django 3.0.2 on 2020-01-14 16:15

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_title', models.CharField(max_length=300)),
                ('tab_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tab_image', models.ImageField(null='TRUE', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_title', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(null='TRUE', verbose_name='date published')),
                ('announcement_attachment', models.FileField(null='TRUE', upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_year', models.IntegerField(choices=[(1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020, verbose_name='year graduated')),
                ('batch_image', models.ImageField(null='TRUE', upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'batches',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_abv', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=300)),
                ('course_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_name', models.CharField(max_length=300)),
                ('element_description', models.TextField()),
                ('element_image', models.ImageField(blank='TRUE', null='TRUE', upload_to='uploads/')),
                ('element_attachment', models.FileField(blank='TRUE', null='TRUE', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='PostStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_status', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Post Statuses',
            },
        ),
        migrations.CreateModel(
            name='Traccer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traccer_type', models.CharField(max_length=300)),
                ('traccer_image', models.ImageField(null='TRUE', upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Traccers',
            },
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
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_title', models.CharField(max_length=300)),
                ('reference_description', models.TextField()),
                ('pub_date', models.DateTimeField(null='TRUE', verbose_name='date published')),
                ('reference_image', models.ImageField(null='TRUE', upload_to='uploads')),
                ('reference_attachment', models.FileField(null='TRUE', upload_to='uploads')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Library')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('post_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('post_image', models.ImageField(null='TRUE', upload_to='uploads/')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PostStatus')),
            ],
        ),
        migrations.CreateModel(
            name='BatchImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_image_description', models.CharField(max_length=300)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Batch')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together={('course_id', 'batch_year')},
        ),
    ]
