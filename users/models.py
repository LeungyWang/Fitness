from django.db import models
from ly_app.models import course,coach
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
	vip_name = models.CharField(max_length=50,default="vip_name")
	vip_gender = (('male','男'),('female','女'))
	vip_sex = models.CharField(max_length=10,choices=vip_gender,default='男')
	vip_birthday = models.DateField(default="2019-12-12")
	vip_phone = models.CharField(max_length=30,default="13XXXXXXXXX")
	vip_email = models.EmailField(default="123456@qq.com")
	vip_duriation = models.CharField(max_length=30,default="10")
	vip_level = models.IntegerField(default=1)
	courseById = models.ManyToManyField(course)
	coachById = models.ManyToManyField(coach)
	class Meta:
		ordering = ('-vip_id',)







