from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterUserForm,RegisterUserForm2
from .models import Profile
from django.contrib.auth.models import User

class UserProfileChangeView(generic.UpdateView):
	model=Profile
	fields=["profile_pic","phone","facebook_url","instagram_url",
	"watsaap"]
	template_name="authentication/update_profile.html"
	success_url=reverse_lazy('profile-page')
class UserSettingsChangeView2(generic.UpdateView):
	model=Profile
	fields=["profile_pic","phone","facebook_url","instagram_url",
	"watsaap"]
	template_name="authentication/update_profile.html"

class UserSettingsChangeView(generic.UpdateView):
	form_class=UserChangeForm
	template_name="authentication/edit_user_settings.html"
	success_url=reverse_lazy('profile-page')
	def get_queryset(self):
	 return User.objects.all()

def login_user(request): 
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home page')

		else:
			messages.success(request,('there is an error'))
			return redirect('login-page')
	else:
		return render(request,'authentication/login.html',{})

def logout_user(request):
	messages.success(request,('Succesfully logged out'))
	logout(request)
	return redirect('home page')



def register_user2(request):
	if request.method=='POST':
		form=RegisterUserForm2(request.POST,request.FILES)
		if form.is_valid():
			user=form.save()
			user.refresh_from_db()
			user.profile.profile_pic=form.cleaned_data.get('profile_pic')
			user.profile.phone=form.cleaned_data.get('phone')
			user.save()
			password=form.cleaned_data.get('password1')
			user=authenticate(username=user.username,password=password)
			login(request,user)
			#print(user.profile.profile_pic.url)
			print(user.profile)
			print(user)
			print(user.username)
			return redirect('home page')
	else:
		form=RegisterUserForm2()
	return render(request,'authentication/register_user.html',{'form':form})




def register_user(request):
	if request.method=="POST":
		form=RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username,password=password)
			login(request,user)
			messages.success(request,('Registerd Successfully'))
			return redirect('home page')
	else:
		form=RegisterUserForm()
		return render(request,'authentication/register_user.html',{
		'form':form
		})



