from django.contrib import admin
from filebrowser.sites import site

# Register your models here.
from django.contrib.admin import AdminSite

class UserAdmin(AdminSite):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres.org'
    admin.site.site_title = 'Cms Site Builder | WebPres,org'
    admin.site.index_title = 'Your user admin'



admin_site = UserAdmin(name='user_admin')
