# Generated by Django 2.2.7 on 2020-09-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cis_website', '0002_remove_blog_data_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_data',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
