from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from homepage import models as model

@view_function
def process_request(request):
    searchform = SearchForm()

    template_vars = {
        'searchform': searchform,
    }

    return dmp_render(request, 'search.html', template_vars)


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-field'}))
    ingredients = forms.ModelMultipleChoiceField(queryset=model.Ingredient.objects.all().order_by('ingredient_text'), widget=forms.CheckboxSelectMultiple, required=False)

@view_function
def search(request):
    recipes = model.Recipe.objects.all().order_by('recipe_name')
    qry = model.Recipe.objects.all().order_by('recipe_name')
    meals = model.MEAL_CHOICES
    mealFilter = False

    if request.method == 'GET':
        recipes = []
        ingredients = []
        prelim = []
        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            if searchform.cleaned_data.get('search'):
                qry = qry.filter(recipe_name__icontains=searchform.cleaned_data.get('search'))
            if searchform.cleaned_data.get('ingredients'):
                checked = [ingredients.pk for ingredients in searchform.cleaned_data['ingredients']]
                for item in checked:
                    qry = qry.filter(id=model.RecipeIngredient.objects.all().filter(ingredient=item).values_list('recipe', flat=True))

            for item in qry:
                recipes.append(item)

            template_vars = {
                'recipes': recipes,
                'meals': meals,
                'mealFilter': mealFilter,
            }

            return dmp_render(request, 'browse.html', template_vars)
        else:
            print(searchform.errors)

    template_vars = {
        'recipes': recipes,
        'meals': meals,
        'mealFilter': mealFilter,
    }

    return dmp_render(request, 'browse.html', template_vars)
