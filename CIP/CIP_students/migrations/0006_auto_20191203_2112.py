# Generated by Django 2.2.4 on 2019-12-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CIP_students', '0005_auto_20191203_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerimage',
            name='reg_img',
            field=models.FileField(default='../static/img/logo.svg', null=True, upload_to='media/alter_avatars'),
        ),
    ]