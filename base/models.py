from django.db import models


class User(models.Model):
    email = models.EmailField()
    login = models.CharField(max_length=50, verbose_name='Логин', unique=True)
    password = models.CharField(max_length=50, verbose_name='Пароль')
    phone = models.IntegerField(verbose_name='Номер телефона')
    photo = models.ImageField()
    date_create = models.DateTimeField(auto_now_add=True)


class Ingredients(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование продукта', unique=True)


class Recipes(models.Model):
    describe = models.CharField(max_length=512, verbose_name='Описание')
    timeOfCooking = models.IntegerField()
    rating = models.ImageField(max_length=5)
    picture = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Автор рецепта', related_name='users')
    favourites = models.ManyToManyField(User, verbose_name='Сохраненный рецепт')
    ingredients = models.ManyToManyField(Ingredients, verbose_name='Ингредиенты в рецепте')


class Comments(models.Model):
    content = models.CharField(max_length=512, verbose_name='Текст')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Автор комментария')
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Комментарий к рецепту')


class StepOfCooking(models.Model):
    step = models.IntegerField(verbose_name='Номер шага')
    name = models.CharField(max_length=256, verbose_name='Наименование шага')
    describe = models.CharField(max_length=512, verbose_name='Описание шага')
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Шаги приготовления в рецепте')


