# Generated by Django 2.2 on 2020-07-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.FileField(upload_to='indexbanner/', verbose_name='图片')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='点击跳转')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '首页广告',
                'verbose_name_plural': '首页广告',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='SubPageBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.FileField(upload_to='indexbanner/', verbose_name='图片')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '首页广告',
                'verbose_name_plural': '首页广告',
                'ordering': ['-created_time'],
            },
        ),
    ]
