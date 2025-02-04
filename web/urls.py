from django.contrib import admin
from django.urls import path

from web.views import main_view

from web.views import registration_view

from web.views import auth_view

from web.views import logout_view

urlpatterns = [
    path("", main_view, name = "main"),
    path("registration/",registration_view, name = "registration"),
    path("auth/",auth_view, name = "auth"),
    path("logout/", logout_view, name = "logout")
]
