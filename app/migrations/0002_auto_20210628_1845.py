# Generated by Django 3.2.4 on 2021-06-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerModel',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.IntegerField(unique=True)),
                ('qualification', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('experience', models.IntegerField()),
                ('designation', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.RemoveField(
            model_name='enquirymodel',
            name='id',
        ),
        migrations.AddField(
            model_name='enquirymodel',
            name='eno',
            field=models.AutoField(default=False, primary_key=True, serialize=False),
        ),
    ]
