# Generated by Django 3.1.1 on 2021-02-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_auto_20171012_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingprofile',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
