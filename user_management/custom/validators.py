from ..forms.user_management_forms import UserForm, LoginForm
from ..models.user_management_models import Post
from django.views.decorators.csrf import csrf_exempt
import re
from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token


@csrf_exempt
def username_validation(username):
    #to check if username already exists then notify user
	if User.objects.filter(username= username).exists():
		message = 'This username is already registerd, please try with another username'
		return message

	#to check username
	if not re.match(r"^[a-zA-Z0-9._%+-]{5,30}$", username):
		message= 'Please Enter a Valid Username. \nMust contain min 5 characters and max 30. Letters, digits and @/./+/-/_ only'
		return message
	else:
		return True

@csrf_exempt
def password_validation(password):
    if not re.match(r"^[a-zA-Z0-9_$%+-]{5,10}$", password):
        message= 'Please Enter a Valid Password. \nMust contain min 5 characters and max 10. 1 Letter, 1 digit and 1 special character[_$%+-]'
        return message
    else:
        return True
