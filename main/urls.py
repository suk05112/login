from django.urls import path, include
from django.contrib import admin
from . import views
import social_login.views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('oauth', views.oauth, name="oauth"),
    path('accounts/', include('allauth.urls')),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),


    # path('profile',views.profile, name='profile'),
    #path('about/', views.about, name="about"),
    # path('result/', views.result, name="result"),
]
