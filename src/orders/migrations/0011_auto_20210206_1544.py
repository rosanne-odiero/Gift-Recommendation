# Generated by Django 3.1.1 on 2021-02-06 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20210206_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpurchase',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
