# Generated by Django 2.2.5 on 2019-09-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
