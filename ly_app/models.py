from django.db import models

# Create your models here.
class course(models.Model):
	courseid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30,unique=True)
	tuition = models.IntegerField()
	people = models.IntegerField()
class coach(models.Modle):
	coachid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)