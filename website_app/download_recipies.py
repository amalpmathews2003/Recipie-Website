from bs4 import BeautifulSoup
import threading
import requests
class Recipie:
	def __init__(self,url,category):
		self.type=category
		self.get_recipie(url)
	def get_recipie(self,url):
		r=requests.get(url)
		soup=BeautifulSoup(r.content,'html5lib')
		self.title=soup.find_all('div',{'class':'shopdeal_title'})[0].text
		self.cooking_time=soup.find_all('div',{'class':'recipe_info'})[0].text
		self.servings=soup.find_all('div',{'class':'recipe_info'})[1].text
		l=soup.find_all('table',{"class":"shopdeal_shade"})
		sl=soup.find_all('table',{"class":"shopdeal_shade"})[0]
		s=sl.find('ul').find_all('li')
		self.ingredients=[]
		for i in s:
			self.ingredients.append(i.text)
		
		self.steps=[]
		s=sl.find('ol').find_all('li')
		for i in s:
			self.steps.append(i.text)	
		self.images=[]
		a=soup.find_all('a',{'class':'fancybox'})
		host="https://www.kindmeal.my"
		for i in a:
			self.images.append(host+i.find_all('img')[0]['src'])
		print(self.title)

def scrap2(i,recipies,category):
	recipies.append(Recipie(i.find_all('a')[0]['href'],category))

def scrap(url,recipies,category):
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html5lib')
	s=soup.find_all("div",{"class":"imagecrop_menu"})
	for i in s:
		t=threading.Thread(target=scrap2,args=(i,recipies,category))
		t.start()
		t.join()
	 	#recipies.append(Recipie(i.find_all('a')[0]['href']))

def main(pages=2,category=2):
	recipies=[]
	categorys=["beverage","appetizer","breakfast","bread","dessert",
	"snack","maindish","salad","sidedish","soup"]
	for category in categorys[1:category]:
		print(category)
		url=f"https://www.kindmeal.my/recipes.htm?category={category}"
		for i in range(1,pages):
			if i==1:
				scrap(url,recipies,category)
			else:
				url=f"https://www.kindmeal.my/recipes.htm?page={i}&category={category}"
				scrap(url,recipies,category)

	return recipies
	










