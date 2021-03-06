# Generated by Django 3.1.7 on 2021-07-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0005_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='amount_deposited',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='amount_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lost_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profit_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
