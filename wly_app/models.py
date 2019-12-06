from django.db import models

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
