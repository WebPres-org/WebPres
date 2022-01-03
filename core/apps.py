from django.apps import AppConfig
from apps.hello_world.apps import HelloWorldConfig
from apps.user.apps import UserConfig



class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    label = 'core'

class HelloWorld(HelloWorldConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.hello_world'
    label = 'apps.hello_world'


class AllUsers(UserConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'
    label = 'apps.user'