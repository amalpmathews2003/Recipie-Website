from django.shortcuts import render
from .models import Recipies
from .forms import RecipieForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


def home(request):
	return render(request,'website_app/home.html',{"name":"amal"})

def all_recipies(request,recipie_list=None):
	if recipie_list==None:
		recipie_list=Recipies.objects.get_queryset().order_by('recipie_name')

	pa=Paginator(recipie_list,9)
	page=request.GET.get('page')
	recipie_list=pa.get_page(page)
	return render(request,'website_app/recipie_list.html',
		{'recipie_list':recipie_list})

def recipie_description(request,recipie_id):
	recipie=Recipies.objects.get(recipie_id=recipie_id)
	recipie.view_count+=1
	recipie.save()

	return render(request,'website_app/recipie_desc.html',
		{"recipie":recipie})

def add_recipie(request):
	submitted=False
	if request.method=="POST":
		form=RecipieForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
				'/add_recipie?submitted=True')
		else:
			print('invalid form')
	else:
		form=RecipieForm
		if 'submitted' in request.GET:
			submitted=True 
		return render(request,'website_app/add_recipie.html',
			{'form':form,'submitted':submitted})

def search_recipies(request):
	if request.method=="POST":
		searched=request.POST['recipie']	
		results=Recipies.objects.filter(recipie_name__contains=searched).order_by('recipie_name')
		return all_recipies(request,results)
	else:
		return all_recipies(request)

def my_profile(request):
	return render(request,'website_app/profile.html',{})