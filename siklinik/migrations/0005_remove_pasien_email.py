# Generated by Django 2.0.4 on 2018-05-07 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siklinik', '0004_pasien_kelpas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasien',
            name='email',
        ),
    ]
