# Generated by Django 2.2 on 2020-07-04 03:46

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_keeperservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keeperservice',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='keeperservice',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='specialservice',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='specialservice',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
