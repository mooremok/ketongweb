# Generated by Django 2.2 on 2020-07-04 02:10

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_specialservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='服务内容'),
        ),
        migrations.AlterField(
            model_name='specialservice',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='服务内容'),
        ),
    ]
