from django.db import models
from apps.user.models import User
from PIL import Image
from django.utils.timezone import now


class CoreUserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

