from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from homepage import models as model

@view_function
def process_request(request):
    recipes = model.Recipe.objects.all().order_by('recipe_name')
    meals = model.MEAL_CHOICES
    mealFilter = False
    currentMeal = ''

    if request.urlparams[0]:
        recipeMeals = model.RecipeMeal.objects.filter(meal=request.urlparams[0]).values_list('recipe', flat=True)

        recipes = recipes.filter(id__in=recipeMeals)

        mealFilter = True
        currentMeal = request.urlparams[0]

    template_vars = {
        'recipes': recipes,
        'meals': meals,
        'mealFilter': mealFilter,
        'currentMeal': currentMeal,
    }

    return dmp_render(request, 'browse.html', template_vars)
