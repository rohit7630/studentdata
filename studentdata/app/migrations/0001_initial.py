# Generated by Django 4.1.6 on 2023-02-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField(unique=True)),
                ('emailid', models.EmailField(max_length=50)),
                ('contactno', models.CharField(max_length=10, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=7)),
            ],
        ),
    ]