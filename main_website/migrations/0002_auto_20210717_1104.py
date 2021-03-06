# Generated by Django 3.1.7 on 2021-07-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Country_of_residence',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='driver_license',
            field=models.ImageField(null=True, upload_to='driver_license/%d/'),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(null=True),
        ),
    ]
