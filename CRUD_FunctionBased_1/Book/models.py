from django.db import models

# Create your models here.

class Student(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	roll = models.IntegerField()
	city = models.CharField(max_length=50)
	