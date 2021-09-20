from django import forms
from django.forms import ModelForm
from .models import Recipies


class RecipieForm(ModelForm):
	class Meta:
		model=Recipies
		#fields="__all__"
		fields=('recipie_name','recipie_type','recipie_author',
			'ingredients','steps','cooking_time','main_image')
		
		# labels={
		# 	'recipie_id':'',
		# 	'recipie_name':'',
		# 	'recipie_type':'',
		# 	'recipie_author':'',
		# 	'ingredients':'',
		# 	'steps':'',
		# 	'cooking_time':'',
		# }

		# widgets={
		# 	'recipie_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Recipie-Id'}),
		# 	'recipie_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Recipie-Name'}),
		# 	'recipie_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Recipie-Type'}),
		# 	'recipie_author':forms.TextInput(attrs={'class':'form-control','placeholder':'Recipie-Author'}),
		# 	'ingredients':forms.TextInput(attrs={'class':'form-control','placeholder':'Recipie-Ingredients'}),
		# 	'steps':forms.TextInput(attrs={'class':'form-control','placeholder':'Recipie-Steps'}),
		# 	'cooking_time':forms.TextInput(attrs={'class':'form-control','placeholder':'Cooking-Time'})
		# }