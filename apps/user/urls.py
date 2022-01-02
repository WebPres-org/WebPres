# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 ronyman.com
"""

from django.urls import path
from django.urls import path, include
from . import views
from .views import profile
import apps.user.views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #User
    path("register/", apps.user.views.register_request, name="register"),
    path("login/", apps.user.views.login_request, name="login"),
    path("myprofile/", apps.user.views.profile, name="Myprofile"),
    path('profile/', profile, name='users-profile'),
    path("logout/", apps.user.views.logout_request, name= "logout"),
    path('tinymce/', include('tinymce.urls')),

    # For PasswordPresset

    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset',),
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done',),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm',),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete',),
]