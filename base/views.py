from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'index.html', context=locals())


def registration(request):
    return render(request, 'registration.html', context=locals())