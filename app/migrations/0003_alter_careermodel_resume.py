# Generated by Django 3.2.4 on 2021-06-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210628_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='resume',
            field=models.FileField(default=False, upload_to='resumes/'),
        ),
    ]
