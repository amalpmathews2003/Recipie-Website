from django.shortcuts import render
from .models import Recipies,WebsiteUser
from .forms import RecipieForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.files import File 
from .download_recipies import main
import urllib
import os
import threading

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
		form=RecipieForm(request.POST,request.FILES)
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

def add_to_database2(request,pages=2,category=2):
	recipies=main(pages=2,category=2)
	for r in recipies:
		if Recipies.objects.filter(recipie_name=r.title).exists():
			continue
		recipie=Recipies()
		recipie.recipie_name=r.title
		recipie.recipie_type=r.type
		recipie.servings=r.servings
		recipie.recipie_author=WebsiteUser.objects.get(user_id=1)	
		recipie.ingredients=r.ingredients
		recipie.steps=r.steps
		recipie.cooking_time=r.cooking_time
		images=r.images
		opener=urllib.request.build_opener()
		opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
		urllib.request.install_opener(opener)
		result = urllib.request.urlretrieve(images[0])
		recipie.main_image.save(os.path.basename(images[0]),
			File(open(result[0], 'rb')))
		recipie.save()
		print(recipie)
	print('*'*10)
	return render(request,'website_app/profile.html',{})


def add_to_database(request,pages=2,category=2):
	t=threading.Thread(target=add_to_database2,args=(request,pages,category))
	t.start()
	return render(request,'website_app/home.html',{})
	
