# Generated by Django 2.2.4 on 2019-12-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CIP_students', '0002_auto_20191202_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.FileField(default='../static/img/logo.svg', null=True, upload_to='media/avatars'),
        ),
    ]
