# Generated by Django 4.1.1 on 2022-10-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0003_remove_mahasiswa_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahasiswa',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
