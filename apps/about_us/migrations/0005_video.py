# Generated by Django 2.2 on 2020-07-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0004_honor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('video', models.FileField(upload_to='video/', verbose_name='视频上传')),
                ('upload_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '视频中心',
                'verbose_name_plural': '视频中心',
                'ordering': ['-upload_time'],
            },
        ),
    ]
