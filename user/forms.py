from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterUserForm2(UserCreationForm):
	#birth_date=forms.DateField(help_text="Required Format:YYYY-MM-DD")
	email=forms.EmailField()
	first_name=forms.CharField(max_length=50)
	last_name=forms.CharField(max_length=50)
	phone=forms.CharField(max_length=20)
	profile_pic=forms.ImageField()
	class Meta:
		model=User
		fields=('username','first_name','last_name','email',
			'profile_pic','phone','password1','password2')


class RegisterUserForm(UserCreationForm):
	email=forms.EmailField()
	first_name=forms.CharField(max_length=50)
	last_name=forms.CharField(max_length=50)
	phone=forms.CharField(max_length=20)
	class Meta:
		model=User
		fields=('username','first_name','last_name','email',
			'password1','password2')
	