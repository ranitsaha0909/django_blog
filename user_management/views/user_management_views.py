from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user_management.forms.user_management_forms import UserForm, LoginForm
from user_management.models.user_management_models import Post
from new_blog.models.new_blog_models import Blog
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_management.custom.validators import *
from user_management.custom.custom_decorators import *
from django.contrib.sessions import *
#from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Main Program Starts Here ->


def post_new_user(request): #New User Registration
    if request.method == "POST": #For 2nd time onwards
            form = UserForm(request.POST)
            username= request.POST['username']
            password= request.POST['password']
            #check username with regex
            check_username_validation = username_validation(username)
            if not check_username_validation == True:
                return render(request, 'new_user.html', {'messege': str(check_username_validation) , 'form': form})
            #check password with regex
            check_password_validation=password_validation(password)
            if not check_password_validation == True:
                return render(request, 'new_user.html', {'messege': str(check_password_validation) , 'form': form})
            #check form validation
            if form.is_valid():
                user = User.objects.create_user(username, 'sample', password)
                user.save()
                msg='User Creation Successful'
                return render(request, 'new_user.html', {'messege': msg , 'form': form})
            else:
                return render(request, 'new_user.html', {'messege': 'Invalid Form' , 'form': form})
    else:
        #For 1st time
            form = UserForm()
            return render(request, 'new_user.html', {'form': form})



#Create a Cross-Site Request Forgery Token
@csrf_exempt
def post_user_login(request): #User login procedure

    #Logout user after 5 mins(300secs) of inactivity
    #request.session.set_expiry(300)
    #For 2nd time onwards
    if request.method == "POST":
        #gets data from loginform with name=user
        login_user = request.POST['user']
        #gets data from loginform with name=password
        login_pass = request.POST['password']
        user = authenticate(username=login_user, password=login_pass)
        if user :
            login(request, user)
            # x = Post.objects.filter()
            # return render(request, 'post_user_list.html', {'posts': x})
            #print ("user logged in ")
            #response='user logged in'
            # return JsonResponse({'response':response})
            return HttpResponseRedirect('/user/blog_list')
        else:
            msg = 'Wrong UserID/Password'
            form = LoginForm()
            return render(request, 'user_login.html', {"form":form, 'msg' : msg})
    else:
        #For 1st time
        #post_user_list(self)
        if request.user.is_authenticated(): #checks if already authticated and session not expired
            x = Blog.objects.filter(author_id=request.user.id)
            #start pagination
            page = request.GET.get('page', 1)

            users = paginate_object_list(request, x, 5)
            return render(request, 'post_user_list.html', {'users': users})
            #return render(request, 'post_user_list.html', {'posts': x})
        else:
            form = LoginForm()
            return render(request, 'user_login.html', {'form':form})

def user_logout(request):
        #Simple Logout
        logout(request)
        return HttpResponseRedirect('/user/')
