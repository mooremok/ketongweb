# Generated by Django 2.2 on 2020-07-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0002_auto_20200704_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='tel',
            field=models.CharField(max_length=30, verbose_name='联系方式'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='type',
            field=models.IntegerField(choices=[(1, '建议'), (2, '投诉')], verbose_name='留言类型'),
        ),
    ]
