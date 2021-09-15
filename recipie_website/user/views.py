from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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