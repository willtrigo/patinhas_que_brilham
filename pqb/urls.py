"""Url configuration of the project."""
from django.contrib import admin
from django.urls import path

from .core.views import view_home as home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
