# Generated by Django 4.1.1 on 2022-10-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tendik',
            name='nama',
            field=models.CharField(max_length=100),
        ),
    ]
