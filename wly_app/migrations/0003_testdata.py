# Generated by Django 2.1.5 on 2019-12-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wly_app', '0002_auto_20191204_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
