from django.shortcuts import render

def home1(request):
	return render(request,'temp.html',{})