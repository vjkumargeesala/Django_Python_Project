from django.db import models

# Create your models here.
class Spoll(models.Model):
	name=models.CharField(max_length=100,null=True)
	data=[('Yes','YES'),('No','NO')]
	opt=models.CharField(max_length=3,choices=data)

class rate(models.Model):
	name=models.CharField(max_length=100,null=True)
	data=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]
	rating=models.CharField(max_length=7,choices=data)

class answer(models.Model):
	name=models.CharField(max_length=100,null=True)
	answer=models.CharField(max_length=100,null=True)	

class POLL(models.Model):
	question=models.CharField(max_length=100,null=True)
	data=[('Yes/No','yes/no'),('Answer','answer'),('Rating','rating')]
	category=models.CharField(max_length=10,choices=data,null=True)

class covid(models.Model):
	options=[('Yes','YES'),('No','NO')]
	diffculty_Breathing=models.CharField(max_length=3,choices=options)
	chest_pain=models.CharField(max_length=3,choices=options)
	loss_of_Speech=models.CharField(max_length=3,choices=options)
	loss_of_Taste=models.CharField(max_length=3,choices=options)
	fever=models.CharField(max_length=3,choices=options)
	cold=models.CharField(max_length=3,choices=options)
	dry_cough=models.CharField(max_length=3,choices=options)
	triedness=models.CharField(max_length=3,choices=options)
	sore_throat=models.CharField(max_length=3,choices=options)
	headache=models.CharField(max_length=3,choices=options)
	
class covid_details(models.Model):
	name=models.CharField(max_length=200,null=True)
	data=[('Male','MALE'),('Female','FEMALE'),('Rather not say','RATHER NOT SAY')]
	gender=models.CharField(max_length=20,choices=data,null=True)
	age=models.CharField(max_length=4,null=True)
	city=models.CharField(max_length=200,null=True)
	address=models.CharField(max_length=900,null=True)
	phno=models.CharField(max_length=20,null=True)
	email=models.EmailField(max_length=80,null=True)

	