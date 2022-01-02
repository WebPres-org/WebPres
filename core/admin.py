from django.contrib import admin
from filebrowser.sites import site
from apps.user.models import UserProfile
from apps.user.admin import UserAdmin

class MyAdminSite(UserProfile):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres.org'
    admin.site.site_title = 'Cms Site Builder | WebPres,org'
    admin.site.index_title = 'WebPres Admin'



admin_site = MyAdminSite()
admin.site.register(UserProfile)

