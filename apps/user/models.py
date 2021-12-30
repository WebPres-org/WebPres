from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
#####
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    url = models.URLField(blank=True)
    about = models.TextField()
    avatar = models.ImageField(upload_to='media/uploads')

    def has_avatar(self):
        return Avatar.objects.filter(user=self.user, valid=True).count()

    def __unicode__(self):
        return _("%s's profile") % self.user

    def get_absolute_url(self):
        return reverse("profile_public", args=[self.user])

