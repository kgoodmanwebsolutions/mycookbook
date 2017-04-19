from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from homepage import models as model

@view_function
def process_request(request):

    try:
        recipe = model.Recipe.objects.get(id=request.urlparams[0])
    except model.Recipe.DoesNotExist:
        return HttpResponseRedirect('/homepage/browse/')

    ingredients = model.RecipeIngredient.objects.filter(recipe=request.urlparams[0]).all()

    template_vars = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return dmp_render(request, 'details.html', template_vars)
