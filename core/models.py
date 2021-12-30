from django.db import models
from apps.user.models import UserProfile


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Myprofile(models.Model):
   user_profile = models.ForeignKey(UserProfile, null = False, blank = False, on_delete = models.CASCADE)