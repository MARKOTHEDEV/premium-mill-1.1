# Generated by Django 3.1.7 on 2021-07-18 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0003_bitcoinaddresse_enquiry_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='countryPhoneCode',
            field=models.IntegerField(null=True),
        ),
    ]
