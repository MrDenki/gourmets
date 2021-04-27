from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from base.forms import UserRegistrationForm, UserProfile, UserAuthenticationForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html', context=locals())


def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(reverse('profile'))
    return render(request, 'registration.html', context=locals())


def Authentication(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)

        email = request.POST(['email'])
        password = request.POST(['password'])
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'recipes.html', context=locals())
        return render(request, 'registration.html', context=locals())


def recipe(request):
    return render(request, 'recipes.html', context=locals())


def profile(request):
    form = UserProfile()
    return render(request, 'profile.html', context=locals())