# Generated by Django 2.2 on 2020-07-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_qanda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qanda',
            name='created_time',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
