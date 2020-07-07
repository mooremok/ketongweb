# Generated by Django 2.2 on 2020-07-04 03:09

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='产品名称')),
                ('description', models.TextField(verbose_name='描述')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='服务内容')),
                ('image', models.FileField(blank=True, help_text='该图片用于样式设置，无特别说明时，勿自行上传', null=True, upload_to='images_uploads/', verbose_name='图片上传')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
