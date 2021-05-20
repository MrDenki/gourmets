from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from gourmets import settings

from base.views import index, registration, profile, all_recipes, authentication, logoutuser, recipe, comment

urlpatterns = [
    path('', index, name='home'),
    path('registration/', registration, name='registration'),
    path('authentication/', authentication, name='authentication'),
    path('logoutuser', logoutuser, name='logoutuser'),
    path('profile/', profile, name='profile'),
    path('select_ingredients/', all_recipes, name='allRecipes'),
    re_path('comment/$', comment, name='comment'),
    re_path(r'^recipe/(\d+)', recipe, name='recipe'),
] + staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)