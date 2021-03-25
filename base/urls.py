from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from base.views import index

urlpatterns = [
    path('', index, name='index')
] + staticfiles_urlpatterns()