from django.db import models
from datetime import datetime

# Create your models here.

class Person(models.Model):
	date_registered = models.DateField(blank=True, null=True)
	firstname = models.CharField(max_length = 100)
	middlename = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	birthdate = models.DateField(blank=True, null=True)
	birthplace = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 50)
	status = models.CharField(max_length = 50)

	class Meta:
		db_table = "Person"

class Customer(Person):
	email = models.CharField(max_length = 50)
	password  = models.CharField(max_length = 30)

	class Meta:				
		db_table = "Customer"