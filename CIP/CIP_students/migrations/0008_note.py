# Generated by Django 2.2.4 on 2019-12-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CIP_students', '0007_auto_20191215_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='...')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]