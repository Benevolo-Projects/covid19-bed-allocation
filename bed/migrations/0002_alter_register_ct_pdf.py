# Generated by Django 3.2 on 2021-05-07 18:19

import bed.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='ct_pdf',
            field=models.FileField(blank=True, null=True, upload_to=bed.models.path_and_rename),
        ),
    ]