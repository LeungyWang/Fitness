# Generated by Django 2.1.5 on 2019-12-20 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='login_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User_Login'),
        ),
    ]
