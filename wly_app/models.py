from django.db import models
import django.utils.timezone as timezone
class BodyData(models.Model):
    user_name = models.CharField(max_length=30,primary_key=True)
    hight = models.DecimalField(max_digits=5,decimal_places=1)
    height = models.DecimalField(max_digits=5,decimal_places=1)
    chest = models.DecimalField(max_digits=5,decimal_places=1)
    waist = models.DecimalField(max_digits=5,decimal_places=1)
    hip = models.DecimalField(max_digits=5,decimal_places=1)
    queith = models.DecimalField(max_digits=5,decimal_places=1)
    maxh = models.DecimalField(max_digits=5,decimal_places=1)
    BMI = models.DecimalField(max_digits=5,decimal_places=1)

# Create your models here.
class BodyParts(models.Model):
    partcode = models.CharField(max_length=16,primary_key=True)
    partname = models.CharField(max_length=10)

class BodytestStandard(models.Model):
    partcode = models.ForeignKey("BodyParts",to_field="partcode",on_delete=True,related_name="Parts_Test")
    value = models.IntegerField()
    points = models.IntegerField()
    comment = models.CharField(max_length=60,default="c")

    

class UserPysicalTest(models.Model):
    user_name = models.ForeignKey("users.New_User",to_field="login_name",on_delete=models.CASCADE)
    partcode = models.ForeignKey("BodyParts",to_field="partcode",on_delete=models.CASCADE)
    testdata = models.IntegerField()
    createon = models.DateTimeField('创建日期',default=timezone.now)
    testlevel = models.CharField(max_length=30,default="LV0")
    class Meta:
        unique_together = ["user_name","partcode","createon"]

class starlevel(models.Model):
    starcode = models.CharField(max_length=30,primary_key=True)
    stardisplay = models.CharField(max_length=30)



class GradeLevel(models.Model):
    grade = models.IntegerField("成绩",primary_key=True)
    level = models.CharField("等级",max_length=10)

    def __unicode__(self):
        return self.grade

class Courses(models.Model):
    courseid = models.CharField("课程编号",max_length=30,primary_key=True)
    coursename = models.CharField("课程名称",max_length=30)
    decription = models.CharField("课程介绍",max_length=150,default="")
    pic = models.CharField("图片路径",max_length=150,default="./")

    def __unicode__(self):
        return self.courseid

class PartCourse(models.Model):
    partcode = models.ForeignKey("BodyParts",to_field="partcode",on_delete=models.CASCADE)
    courseid = models.ForeignKey("Courses",to_field="courseid",on_delete=models.CASCADE)
    courselevel = models.CharField("课程等级",max_length=10)
    frequency = models.CharField("次数",max_length=30)
    class Meta:
        unique_together = ["partcode","courseid","courselevel"]

    def __unicode__(self):
        return self.partcode,self.courseid



