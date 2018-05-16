from django.db import models
from django.utils import timezone
#SSimport uuid
#from auth import User

class Post(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    #user_unq_id=models.UUIDField(default=uuid.uuid4, unique=True),

    def publish(self):
        #self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user

# class Blog(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     def publish(self):
#         #self.created_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.user
