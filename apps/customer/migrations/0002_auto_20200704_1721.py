# Generated by Django 2.2 on 2020-07-04 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': '客户类型', 'verbose_name_plural': '客户类型'},
        ),
    ]
