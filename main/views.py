from django.shortcuts import render
import requests
from .models import Users
from .forms import UserForm
from django.template import loader

# Create your views here.
def home(request):
     return render(request, 'main/home.html')

def main(request):
    return render(request,'main/main.html')

def login(request):

     qs = Users.objects.all()
     if qs.filter(account=request.GET.get('account')) :

          print("유저 있음")
          return redirect('profile')
     else :
     # if request.method == 'GET':
          user = UserForm(request.GET)
          if user.is_valid():
               post = user.save(commit=False)

               #nickname
               user.nickname = request.GET.get('nickname')
               request.session['nickname']=user.nickname

               # account
               user.account = request.GET.get('account')
               request.session['account']=user.account

               #image
               user.profileimage = request.GET.get('profileimage')
               request.session['profileimage']=user.profileimage

               post.save()
               context = {    'user.nickname':user.nickname,
                              'user.account':user.account,
                              'user.profileimage':user.profileimage,
                          }
               # print( request.GET.get('account'))
               # return render(request, 'social_login/home.html')
               return redirect('home')

def oauth(request):
    return render(request,'main/oauth.html')

def camera(request):
    return render(request,'main/oauth.html')

def profile(request):
    location_lat = request.GET.get('latitude')
    location_lon = request.GET.get('longtitude')
    print(location_lat);
    print(location_lon);
    return render(request, 'main/profile.html')
