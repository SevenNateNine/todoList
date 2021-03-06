# Generated by Django 3.1 on 2020-08-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200)),
                ('task_description', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('updated_date', models.DateTimeField(verbose_name='date updated')),
                ('completed', models.BooleanField()),
            ],
        ),
    ]
