from django.db import models
#from django.contrib.auth.models import User

class WebsiteUser(models.Model):
	user_id=models.CharField(max_length=10,primary_key=True,unique=True)
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20,blank=True,null=True)
	phone=models.CharField(max_length=20,blank=True,null=True)
	email=models.EmailField(max_length=50,blank=True,null=True)
	place=models.CharField(max_length=20,blank=True,null=True)
	profile_pic=models.ImageField(upload_to=f'files/{user_id}',null=True,blank=True)
	def __str__(self):
		return self.first_name+' '+self.last_name

class Recipies(models.Model):
	recipie_id=models.AutoField(primary_key=True)
	recipie_name=models.CharField(max_length=100)
	recipie_type=models.CharField(max_length=20,blank=True)
	recipie_author=models.ForeignKey(WebsiteUser,on_delete=models.CASCADE)
	view_count=models.PositiveIntegerField(default=0,blank=True)
	like_count=models.PositiveIntegerField(default=0,blank=True)
	ingredients=models.TextField()
	steps=models.TextField()
	cooking_time=models.CharField(max_length=20,null=True)
	#uploaded_time=models.DateTimeField()	
	main_image=models.ImageField(upload_to=f"files/{recipie_id}",null=True,blank=True)

	def __str__(self):
		return self.recipie_name



