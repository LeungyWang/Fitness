from django.db import models

# Create your models here.

class User(models.Model):

	vip_id = models.AutoField(primary_key=True)

	vip_name = models.CharField(max_length=50)

	vip_gender = (('male','男'),('female','女'))

	vip_sex = models.CharField(max_length=10,choices=vip_gender)

	vip_birthday = models.DateField()

	vip_phone = models.CharField(max_length=30)

	vip_email = models.EmailField(unique=True)

	vip_duriation = models.CharField(max_length=30)

	vip_level = models.IntegerField()

	class Meta:
		ordering = ('-vip_id',)
