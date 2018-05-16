from django.db import models
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.FileField(blank=True, null=True, upload_to='media/pictures/')

    def publish(self):
        #self.created_date = timezone.now()
        self.save()

    # def __str__(self):
    #     return self.user
