# Generated by Django 3.2.4 on 2021-09-20 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_profile_pic'),
        ('website_app', '0004_auto_20210914_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipies',
            name='recipie_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]