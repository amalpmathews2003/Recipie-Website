from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home page"),
    path('recipie-all',views.all_recipies,name='recipie-list'),
    path('recipie/<int:recipie_id>',views.recipie_description,
        name="recipie-discription"),
    path('add_recipie',views.add_recipie,name="add-recipie"),
    path('search_recipies',views.search_recipies,name="search-recipies"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)