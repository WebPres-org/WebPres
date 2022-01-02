from django.contrib.admin.apps import AdminConfig
from core.admin import core_admin

class MyAdminConfig(AdminConfig):
    default_site = 'core.admin.MyadminSite'
    #default_site = 'apps.hello_world.hello_admin'
    #default_site = 'apps.user.user_admin'


