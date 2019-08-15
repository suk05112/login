from django.shortcuts import render, redirect
import requests
from .models import Users
from .forms import UserForm
# from django.core import serializers
from django.http import HttpResponse
from django.template import loader
# from django.contrib.auth.models import Users


# Create your views here.

def home(request):
     return render(request, 'social_login/home.html')

def profile(request):
     
     return render(request, 'social_login/profile.html')

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
               return render(request, 'social_login/home.html', context)

# def google(requests):
#      user=Users
     
     
#      print("구글")
#      print(user.username)
#      return render(request, 'social_login/profile.html')
               # info = Users.objects

               # return render(request,'social_login/profile.html', {'info': info})


               # return HttpResponse(template.render(context, request))

          


     #      user = Users()
               
     #      #nickname
     #      user.nickname = request.GET.get('nickname')
     #      request.session['nickname']=user.nickname
     #      nick=request.session.get('nickname')
               
     #      #account
     #      user.account = request.GET.get('account')
     #      request.session['account']=user.account 

     #      #image
     #      user.profileimage = request.GET.get('profileimage')
     #      request.session['profileimage']=user.profileimage
     #      # nickname=request.session.get('image')

     #      user.save()

     #      print(profile)
     #      #test print
     #      print(nick)
     #      print(user.nickname)
     #      print(user.account)
     #      print(user.profileimage)
     #      print(request.session['profileimage'])

  
     # return HttpResponse("저장 성공")
     # return render(request, 'social_login/login.html', {'account': account})
     # return redirect('profile')


# def login(request):
    
#      if request.method == 'GET':
#      #    acoount = request.POST['account']
#           nickname = request.GET['nickname']
#      #      request.session['nickname']='nickname'
#      #      nick=session.get('nickname')
#      #      console.log(nick)
#      # #    nickname = request.GET['nickname']
#      #    profileimage = request.GET['profileimage']
#           print(nickname)
#           print(request.GET['nickname']
#      #    print(account)
         
#           return render(request, 'social_login/profile.html')

#          def login(request):
#    username = ‘not logged in’
#       if request.method == ‘POST’:
#       MyLoginForm = LoginForm(request.POST)      
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data[‘username’]
#          request.session[‘username’] = username
#       else:
#          MyLoginForm = LoginForm()
#    return render(request, ‘loggedin.html’, {“username” : username}

     #     return HttpResponse(request.GET['nickname'])
     # print(request.GET['account'])

     # print(request.GET['profileimage'])
     # print(request.GET['nickname'])

     # user = Users()
     # user.account = request.GET['account']
     # user.profileimage = request.GET['profileimage']
     # user.nickname = request.GET['nickname']
     # user.save()
     # print(user)

     
     #posts = Users.objects.filter(published_at__isnull=False).order_by('-published_at')
     #post_list = serializers.serialize('json', posts)
     #return HttpResponse(post_list, content_type="text/json-comment-filtered")
     #  return render(request, 'social_login/home.html')



