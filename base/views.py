from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from base.forms import UserRegistrationForm, UserProfile, UserAuthenticationForm
from django.contrib.auth import authenticate, login

from base.models import User


def index(request):
    # user = User()
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        email = request.POST('email')
        password = request.POST('password')
        user = authenticate(request, email=email, password=password)
        # if form.email == user.email and form.password == user.password:
        if user is not None:
            login(request, user)
            return render(request, 'select_ingredients.html', context=locals())
        return render(request, 'registration.html', context=locals())
    return render(request, 'index.html', context=locals())


def registration(request):
    form = UserRegistrationForm()
    user = User()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.login = request.POST.get("email").split('@')[0]
            user.name = request.POST.get("email").split('@')[0]
            user.save()
            return HttpResponse(reverse('profile'))
    return render(request, 'registration.html', context=locals())


# def Authentication(request):
#     user = User()
#     if request.method == 'POST':
#         form = UserAuthenticationForm(request.POST)
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(request, email=email, password=password)
#         # if email == user.objects.email and password == user.objects.password:
#         if user is not None:
#             login(request, user)
#             return render(request, 'select_ingredients.html', context=locals())
#         return render(request, 'registration.html', context=locals())
#     return HttpResponse("Reload")


def recipe(request):
    return render(request, 'select_ingredients.html', context=locals())


def profile(request):
    return render(request, 'profile.html', context=locals())