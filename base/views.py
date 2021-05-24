from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from base.forms import RegistrationForm, ProfileFrom
from django.contrib.auth import authenticate, login, logout


from base.models import Users, Recipes, Ingredients, recipesIngredients, StepOfCooking, Comments


def index(request):
    return render(request, 'index.html', context=locals())


def registration(request):
    form = RegistrationForm()
    user = Users()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # if user.email != request.POST.get("email"):
        if form.is_valid():
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.login = request.POST.get("email").split('@')[0]
            user.username = request.POST.get("email").split('@')[0]
            django_user = User.objects.create_user(username=user.login, email=user.email, password=user.password)

            user.save()
            django_user.save()
            subject = """Подтверждение почты"""
            content = f'Мы рады, что зарегистрировались на нашем сайте!\n' \
                      f'Ваш логин:\t{user.login}\n' \
                      f'Ваш пароль:\t{user.password}'
            send_mail(subject, content, 'IGourmet@yandex.ru', [f'{user.email}'], fail_silently=True)

            login(request, django_user)
            return redirect('allRecipes')
        else:
            messages.error(request, 'Такой пользователь уже существует!')
    return render(request, 'registration.html', context=locals())


def authentication(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('allRecipes')
        else:
            messages.error(request, 'Неверно введены данные!')
    return render(request, 'index.html', context=locals())


# @login_required() погуглить как использовать
def all_recipes(request):
    reipes = Recipes.objects.all()
    return render(request, 'select_ingredients.html', context=locals())


def recipe(request, id):
    recIngr = recipesIngredients.objects.filter(recipes_id=id)
    steps = StepOfCooking.objects.filter(recipes_id=id).order_by('step')
    coment = Comments.objects.filter(recipes_id=id)
    return render(request, 'recipe.html', context=locals())


@login_required()
def profile(request, id):
    profileInfo = Users.objects.get(id=id) # ProfileFrom()
    return render(request, 'profile.html', context=locals())


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
def comment(request):
    userComment = Comments.objects.all()
    # coment = Comments.objects.all()
    if request.method == 'POST':
        userComment.content = request.POST.get('i2')
        userComment.recipes_id = 1
        userComment.user_id = 18
        userComment.save()
    # return redirect('recipe', 1)
    return render(request, 'recipe.html', context=locals())


def about_us(request):
    return render(request, 'about_us.html', context=locals())