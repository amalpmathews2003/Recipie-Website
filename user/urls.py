from django.urls import path
from . import views


urlpatterns = [
    path('login-user',views.login_user,name="login-page"),
    path('logout-user',views.logout_user,name="logout-page"),
    path('register-user',views.register_user2,name="register-user"),
    path('<int:pk>/edit-user-profile',views.UserProfileChangeView.as_view(),
        name="edit-user-profile"),
     path('<int:pk>/edit-user-settings',views.UserSettingsChangeView.as_view(),
        name="edit-user-settings"),
]
    