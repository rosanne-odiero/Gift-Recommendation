# Generated by Django 3.1.1 on 2021-02-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.CharField(max_length=10)),
                ('stockcode', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=5)),
            ],
        ),
    ]
