# Generated by Django 4.1.6 on 2023-02-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contactno',
            field=models.BigIntegerField(max_length=10),
        ),
    ]