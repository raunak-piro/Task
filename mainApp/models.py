from django.db import models
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
class Client(models.Model):
	full_name=models.CharField(max_length=30)
	company=models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	email=models.EmailField(max_length=50)
	def __str__(self):
		return self.full_name

class Employee(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=50)
	phone = models.CharField(max_length=15)
	salary=models.IntegerField()
	city=models.CharField(max_length=30,default="",null=True,blank=True)
	state=models.CharField(max_length=30,default="",null=True,blank=True)
# Create your models here.




class Project(models.Model):
	project_id=models.CharField(max_length=30)

	project_title=models.CharField(max_length=30)
	department=models.CharField(max_length=30,null=True)
	priority=models.CharField(max_length=30,null=True)
	client=models.CharField(max_length=30,null=True)
	From_Date=models.DateField(null=True)
	To_Date=models.DateField(null=True)
	work_status=models.CharField(max_length=30,null=True)
	def __str__(self):
		return self.project_title

