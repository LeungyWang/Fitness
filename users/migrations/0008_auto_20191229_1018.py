# Generated by Django 2.1.8 on 2019-12-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191229_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='vip_email',
            field=models.EmailField(default='123456@qq.com', max_length=254),
        ),
    ]
