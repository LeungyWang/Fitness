from django.db import models
# Create your models here.
class User_Login(models.Model):
	user_name = models.CharField(max_length=30, primary_key=True)
	user_password = models.CharField(max_length=256, default="123456")

class Admin_Login(models.Model):
	admin_name = models.CharField(max_length=30, primary_key=True)
	admin_password = models.CharField(max_length=30)

class New_User(models.Model):
	vip_id = models.AutoField(primary_key=True)
	login_name = models.ForeignKey("User_Login",to_field="user_name",on_delete=models.CASCADE,unique=True)
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







