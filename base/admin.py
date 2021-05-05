from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(CategoriesOfIngredients)
admin.site.register(Ingredients)
admin.site.register(CategoriesOfDishes)
admin.site.register(Recipes)
admin.site.register(Comments)
admin.site.register(StepOfCooking)

