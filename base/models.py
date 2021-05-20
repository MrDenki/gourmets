from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=50, verbose_name='Логин', unique=True, null=True, blank=True)
    password = models.CharField(max_length=10,verbose_name='Пароль')
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True, blank=True, auto_now=True)


class CategoriesOfIngredients(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование категории', unique=True)


class Ingredients(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование продукта', unique=True)
    categoryOfIngredient = models.ForeignKey(CategoriesOfIngredients, on_delete=models.DO_NOTHING, verbose_name='Наименование категории ингредиента', null=True, blank=True)


class CategoriesOfDishes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория', unique=True)


class Recipes(models.Model):
    title = models.CharField(max_length=512, verbose_name='Наименование блюда', null=False, blank=False)
    describe = models.CharField(max_length=2048, verbose_name='Описание')
    timeOfCooking = models.CharField(max_length=32, verbose_name='Время приготовления')
    rating = models.IntegerField(null=True, blank=True)
    picture = models.CharField(max_length=512, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, blank=True, null=True) #
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name='Автор рецепта', related_name='users', default=1, blank=True, null=True) #
    dishCategory = models.ForeignKey(CategoriesOfDishes, on_delete=models.DO_NOTHING, verbose_name='Наименование категории блюда', null=True, blank=True)
    favourites = models.ManyToManyField(Users, verbose_name='Сохраненный рецепт', null=True, blank=True)


class recipesIngredients(models.Model):
    ingredients = models.ForeignKey(Ingredients, verbose_name='Ингредиенты в рецепте', on_delete=models.DO_NOTHING)
    recipes = models.ForeignKey(Recipes, verbose_name='Id Рецепта', on_delete=models.CASCADE)
    amount = models.CharField(max_length=64, verbose_name='Количество грамм ингредиента')


class Comments(models.Model):
    content = models.CharField(max_length=512, verbose_name='Текст')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name='Автор комментария')
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Комментарий к рецепту')


class StepOfCooking(models.Model):
    photo = models.CharField(max_length=512, null=True, blank=True)
    step = models.IntegerField(verbose_name='Номер шага')
    name = models.CharField(max_length=255, verbose_name='Наименование шага', null=True, blank=True)
    describe = models.CharField(max_length=512, verbose_name='Описание шага')
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Шаги приготовления в рецепте')