from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic=models.ImageField(upload_to=f'files/{user}',
		null=True,blank=True)
	phone=models.CharField(max_length=20,blank=True,null=True)
	#facebook_url=models.CharField(max_length=50,blank=True,null=True)
	#instagram_url=models.CharField(max_length=50,blank=True,null=True)
	#watsaap=models.CharField(max_length=50,blank=True,null=True)
	def __str__(self):
		return self.user.username



@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
	try:
		instance.profile.save()	
	except:
		Profile.objects.create(user=instance)




