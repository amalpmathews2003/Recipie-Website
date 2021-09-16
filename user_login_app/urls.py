from django.urls import path,include
from . import views
    
urlpatterns = [
    path('login',views.home1,name="home1")
]   
