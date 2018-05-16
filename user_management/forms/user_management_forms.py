from django.contrib.auth.models import User
from django import forms
from ..models.user_management_models import Post

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password',)

class LoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ('title', 'text')
