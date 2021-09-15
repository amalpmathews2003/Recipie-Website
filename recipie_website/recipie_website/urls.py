from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-login/',include('user.urls')),
    path('user/',include('django.contrib.auth.urls')),
    #path('user/',include('user_login_app.urls')),
    
    
    path('',include('website_app.urls')),
    
]   
