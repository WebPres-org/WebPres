from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)



# Create your models here.
class Profile(models.Model):
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    #user = models.ForiegnKey(User)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images",default="default/user.png")


def __str__(self):
        return self.user.username