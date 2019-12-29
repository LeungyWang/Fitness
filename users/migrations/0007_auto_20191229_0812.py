# Generated by Django 2.1.8 on 2019-12-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_new_user_coachbyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='vip_birthday',
            field=models.DateField(default='2019-12-12'),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='vip_duriation',
            field=models.CharField(default='10', max_length=30),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='vip_email',
            field=models.EmailField(default='123456@qq.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='vip_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='vip_name',
            field=models.CharField(default='vip_name', max_length=50),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='vip_phone',
            field=models.CharField(default='13XXXXXXXXX', max_length=30),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='vip_sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=10),
        ),
    ]
