from django.apps import AppConfig


class HelloWorldConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.hello_world'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

class FileBrowserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filebrowser'

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'