from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from gourmets import settings

from base.views import index, registration, profile, all_recipes, authentication, logoutuser, recipe, comment, about_us

urlpatterns = [
    path('', index, name='home'),
    path('registration/', registration, name='registration'),
    path('authentication/', authentication, name='authentication'),
    path('logoutuser', logoutuser, name='logoutuser'),
    re_path(r'^profile/(\d+)', profile, name='profile'),
    path('select_ingredients/', all_recipes, name='allRecipes'),
    path('comment/', csrf_exempt(comment), name='comment'),
    re_path(r'^recipe/(\d+)', recipe, name='recipe'),
    path('about_us', about_us, name='about_us')
] + staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)