# Generated by Django 4.1.1 on 2022-10-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pimpinan',
            name='fakultas',
        ),
        migrations.RemoveField(
            model_name='pimpinan',
            name='nip',
        ),
        migrations.AlterField(
            model_name='pimpinan',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
