from django.db import models

# Create your models here.
class course(models.Model):
    courseid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    spendtime=models.CharField(max_length=30, unique=True)
    starttime = models.CharField(max_length=30, unique=True)
    classroom = models.CharField(max_length=30,unique=True)

    person = models.IntegerField()

class coach(models.Model):
    coachid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = (('male', '男'), ('female', '女'))
    sex= models.CharField(max_length=10,choices=gender)
    age = models.IntegerField()
    sense = models.CharField(max_length=30)
    createtime = models.DateTimeField(verbose_name=u'接收数据时间', auto_now_add=True, db_index=True)
