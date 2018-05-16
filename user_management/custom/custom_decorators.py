from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ..forms.user_management_forms import UserForm, LoginForm
from ..models.user_management_models import Post
from new_blog.models.new_blog_models import Blog
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..custom.validators import *
from django.contrib.sessions import *
#from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate_object_list(request, object, post_per_page):
    page = request.GET.get('page', 1)
    paginator = Paginator(object, post_per_page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return users
