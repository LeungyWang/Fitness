# Generated by Django 2.1.8 on 2019-12-28 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wly_app', '0024_auto_20191228_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodydata',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.New_User', to_field='login_name'),
        ),
    ]
