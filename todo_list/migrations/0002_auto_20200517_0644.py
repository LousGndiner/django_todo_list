# Generated by Django 2.2.7 on 2020-05-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('employer', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
