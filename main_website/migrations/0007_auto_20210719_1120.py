# Generated by Django 3.1.7 on 2021-07-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0006_auto_20210719_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='amount_deposited',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='amount_made',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lost_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profit_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]