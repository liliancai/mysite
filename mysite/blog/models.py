from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
	name=models.CharField(max_length=100)

class Category(models.Model):
	name=models.CharField(max_length=100)

class Post(models.Model):
	title=models.CharField(max_length=70)
	body=models.TextField()
	excerpt=models.CharField(max_length=200,blank=True)
	created_time=models.DateTimeField()
	modified_time=models.DateTimeField()

	#forgeinkeys
	category=models.ForeignKey(Category)
	tags=models.ManyToManyField(Tag,blank=True)

	#have to import from django's official
	author=models.ForeignKey(User)
