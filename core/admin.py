from django.contrib import admin
from filebrowser.sites import site
from apps.user.models import Profile
from django.contrib.admin import AdminSite

class MyAdminSite(Profile):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres.org'
    admin.site.site_title = 'Cms Site Builder | WebPres,org'
    admin.site.index_title = 'WebPres Admin'


## this line to add app to the admin
admin_site = MyAdminSite(admin)


