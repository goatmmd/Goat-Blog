# Generated by Django 3.2 on 2022-05-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20220507_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profiles_pic', verbose_name='Profile_Pic'),
        ),
    ]
