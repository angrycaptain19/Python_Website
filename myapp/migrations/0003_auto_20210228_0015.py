# Generated by Django 3.1.7 on 2021-02-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210227_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
