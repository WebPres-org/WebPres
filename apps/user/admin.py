
# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# Register your models here.
#from .models import User
from .models import Profile
admin.site.register(Profile)




# Register your models here.
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres.org'
    admin.site.site_title = 'CMS Site Builder | WebPres'
    admin.site.index_title = 'WebPres Site Builder'


admin_site = MyAdminSite()



##Add New

