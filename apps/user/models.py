from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
#####

class UserProfile(models.Model):
   User = models.OneToOneField(User, on_delete = models.CASCADE)