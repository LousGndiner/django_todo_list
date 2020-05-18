from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
'''
class List(models.Model):
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    def __str__(self):
        return self.item
'''

class AlumniModel(models.Model):
    lastName    = models.CharField(max_length = 200)
    firstName   = models.CharField(max_length = 200)
    gender      = models.CharField(max_length = 200)
    year        = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    course      = models.CharField(max_length = 200)
    job         = models.CharField(max_length = 200)
    employer    = models.CharField(max_length = 200)

    def __str__(self):
        return self.lastName + " " + self.firstName

#perform the following after editing the model:
#python3 manage.py makemigrations
#python3 manage.py migrate