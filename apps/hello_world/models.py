from django.db import models
from filebrowser.settings import ADMIN_THUMBNAIL
from filebrowser.base import FileObject
from filebrowser.fields import FileBrowseField



# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


