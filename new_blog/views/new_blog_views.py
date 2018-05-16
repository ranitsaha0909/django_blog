from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ..forms.new_blog_forms import BlogForm
from new_blog.models.new_blog_models import Blog
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from ..custom.validators import *
from django.contrib.sessions import *
#from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@csrf_exempt
def blog_post(request):
    if request.method == "POST": #for 2nd time or more visits
        form = BlogForm(request.POST, request.FILES)
        if not request.user.is_authenticated():
            msg = "Please log in to continue"
            return render(request, 'blog_form.html', {'form': form, 'msg':msg}) #if not logged in

        if form.is_valid(): # if the inputs r valid then post
            post = form.save(commit=False)
            path = post.picture
            image_extension = (".jpeg", ".jpg", ".bmp", ".png")
            #print (path)
            if not str(path).endswith(image_extension):
                msg = "Invalid Image Format"
                return render(request, 'blog_form.html', {'form': form, 'msg':msg})

            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            msg = 'Posted Successfully'
            return render(request, 'blog_form.html', {'form': form, 'msg':msg})
        else: # if inputs are invalid
            msg = 'Failed. \n Invalid Form'
            return render(request, 'blog_form.html', {'form': form, 'msg':msg})
    else: # for first visit
        form = BlogForm()
        return render(request, 'blog_form.html', {'form': form})


def blog_view(request, blog_id):
    if request.user.is_authenticated(): #checks if already authticated and session not expired
        x = Blog.objects.get(id=blog_id)
        #print (x.picture)
        return render(request, 'blog_detail.html', {'post': x})
    else:
        return render(request, 'plz_login.html')


def edit_post(request, blog_id):
    data=Blog.objects.get(id=blog_id)
    message = ''
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=data)
        if request.user.is_authenticated():
            try:
                if form.is_valid():
                    post = form.save(commit=False)
                    path = post.picture
                    image_extension = (".jpeg", ".jpg", ".bmp", ".png")
                    print (form)
                    if not str(path).endswith(image_extension):
                        msg = "Invalid Image Format"
                        return render(request, 'blog_form.html', {'form': form, 'msg':msg})

                    post.author = request.user
                    post.created_date = timezone.now()
                    post.save()
                    msg = "Your Blog Post Was Successfully Edited"
                    return render(request, 'blog_form.html', {'form': form, 'msg':msg})
                    # print (form)
                    # form.save()
                    # message = "Your Blog Post Was Successfully Edited"
            except Exception as e:
                message = 'Your Post Was Not Edited Due To An Error'

        else:
            return render(request, 'plz_login.html')
    else:
        form = BlogForm(instance=data)
        if form.is_valid():
            form.save()
    return render(request, 'blog_edit.html', {'form': form , 'msg' : message})
