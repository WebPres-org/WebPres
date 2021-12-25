from django.db import models
from filebrowser.settings import ADMIN_THUMBNAIL
from filebrowser.base import FileObject
from filebrowser.fields import FileBrowseField



# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


def image_thumbnail(self, obj):
    if obj.image and obj.image.filetype == "Image":
        return '<img src="%s" />' % obj.image.version_generate(ADMIN_THUMBNAIL).url
    else:
        return ""
image_thumbnail.allow_tags = True
image_thumbnail.short_description = "Thumbnail"



def image(self):
    if self.image_upload:
        return FileObject(self.image_upload.path)
    return None


def image_thumbnail(self, obj):
    if obj.image_upload:
        image = FileObject(obj.image_upload.path)
        if image.filetype == "Image":
            return '<img src="%s" />' % image.version_generate(ADMIN_THUMBNAIL).url
    else:
        return ""
image_thumbnail.allow_tags = True
image_thumbnail.short_description = "Thumbnail"




class BlogEntry(models.Model):
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True)
    document = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=[".pdf",".doc"], blank=True)



def new(request, fileobjects):
     if self.image_upload:
        return FileObject(self.image_upload.path)


class Media:
    js = ['/path/to/tinymce/jscripts/tiny_mce/tiny_mce.js', '/path/to/your/tinymce_setup.js',]