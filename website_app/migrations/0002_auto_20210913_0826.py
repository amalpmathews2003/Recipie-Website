# Generated by Django 3.2.4 on 2021-09-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipies',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='files/<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='websiteuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='files/<django.db.models.fields.CharField>'),
        ),
    ]
