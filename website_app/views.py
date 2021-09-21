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
import sys
sys.path.append('../user')
from user.models import Profile

def home(request):
	return render(request,'website_app/home.html',
		{})

def all_recipies(request,recipie_list=None):
	if recipie_list==None:
		recipie_list=Recipies.objects.get_queryset().order_by('recipie_name')

	pa=Paginator(recipie_list,12)
	page=request.GET.get('page')
	recipie_list=pa.get_page(page)
	return render(request,'website_app/recipie_list.html',
		{'recipie_list':recipie_list})

def recipie_description(request,recipie_id):
	recipie=Recipies.objects.get(recipie_id=recipie_id)
	recipie.view_count+=1
	recipie.save()
	if type(recipie.ingredients)==str:
		ingredients=list(recipie.ingredients.split(','))
	if type(recipie.steps)==str:
		steps=list(recipie.steps.split(','))
	try:
		ingredients=eval(recipie.ingredients)
		steps=eval(recipie.steps)
	except:
		pass
	return render(request,'website_app/recipie_desc.html',
		{"recipie":recipie,"ingredients":ingredients,"steps":steps})

def add_recipie(request):
	submitted=False
	if request.method=="POST":
		form=RecipieForm(request.POST,request.FILES)
		if form.is_valid():
			f=form.save(commit=False)
			f.recipie_author=request.user.profile
			#print(f.recipie_author)
			f.save()
			#print(f.recipie_author)
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
		results=Recipies.objects.filter(recipie_name__icontains=searched).order_by('recipie_name')
		return all_recipies(request,results)
	else:
		return all_recipies(request)

def filter_recipies(request,type=None):
	if type:
		results=Recipies.objects.filter(recipie_type__icontains=type).order_by('recipie_name')
		return all_recipies(request,results)
	else:
		return all_recipies(request)

def my_profile(request):
	own_recipies=Recipies.objects.filter(recipie_author_id=request.user.id)
	return render(request,'website_app/profile.html',
		{"own_recipies":own_recipies})

def add_to_database2(request=None,pages=2,category=2):
	recipies=main(pages,category)
	for r in recipies:
		if Recipies.objects.filter(recipie_name=r.title).exists():
			continue
		recipie=Recipies()
		recipie.recipie_name=r.title
		recipie.recipie_type=r.type
		recipie.servings=r.servings
		recipie.recipie_author=Profile.objects.get(user_id=1)	
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


def add_to_database(request,pages=2,category=2):
	t=threading.Thread(target=add_to_database2,args=(pages,category))
	t.start()
	return render(request,'website_app/home.html',{})
	
