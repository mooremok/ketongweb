# Generated by Django 2.2 on 2020-07-04 03:55

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_auto_20200704_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCulture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(verbose_name='描述')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('image', models.FileField(blank=True, help_text='该图片用于样式设置，无特别说明时，勿自行上传', null=True, upload_to='images_uploads/', verbose_name='图片上传')),
            ],
            options={
                'verbose_name': '企业文化',
                'verbose_name_plural': '企业文化',
            },
        ),
    ]
