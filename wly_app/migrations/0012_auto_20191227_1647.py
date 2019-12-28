# Generated by Django 2.1.5 on 2019-12-27 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191220_1724'),
        ('wly_app', '0011_gradelevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpysicaltest',
            name='createon',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AddField(
            model_name='userpysicaltest',
            name='testlevel',
            field=models.CharField(default='LV0', max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='userpysicaltest',
            unique_together={('user_name', 'partcode', 'createon')},
        ),
    ]
