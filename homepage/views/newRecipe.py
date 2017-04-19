from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from homepage import models as model

# Create ingredient object with name, measurement, name
# Put ingredients in an array

@view_function
def process_request(request):
    request.session.flush()
    recipeInfoForm = RecipeInfo()

    template_vars = {
        'recipeInfoForm': recipeInfoForm,
    }

    return dmp_render(request, 'newRecipe.html', template_vars)

@view_function
def info(request):
    recipeInfoForm = RecipeInfo()

    if request.method == 'POST':
        recipeInfo = RecipeInfo(request.POST)
        if recipeInfo.is_valid():
            recipe_name = recipeInfo.cleaned_data.get('recipeName')
            cook_time = recipeInfo.cleaned_data.get('cookTime')
            recipe_source = recipeInfo.cleaned_data.get('source')
            meals = recipeInfo.cleaned_data['meals']

            request.session['recipe_name'] = recipe_name
            request.session['cook_time'] = cook_time
            request.session['source'] = recipe_source
            request.session['meals'] = meals

            addIngredientForm = AddIngredient()
            createIngredientForm = CreateIngredient()

            template_vars = {
                'addIngredientForm': addIngredientForm,
                'createIngredientForm': createIngredientForm,
                'recipe_name': request.session['recipe_name'],
                'cook_time': request.session['cook_time'],
                'source': request.session['source'],
                'meals': request.session['meals'],
            }

            return dmp_render(request, 'newRecipe.ingredients.html', template_vars)

        else:
            print(recipeInfo.errors)

    template_vars = {
        'recipeInfoForm': recipeInfoForm,
    }

    return dmp_render(request, 'newRecipe.html', template_vars)

@view_function
def ingredients(request):
    recipeInfoForm = RecipeInfo()
    addIngredientForm = AddIngredient()
    createIngredientForm = CreateIngredient()

    if 'ingredient_array' not in request.session:
        request.session['ingredient_array']=[]

    if request.method == 'POST':

        if 'addIngredient' in request.POST:
            ingredientForm = AddIngredient(request.POST)

            if ingredientForm.is_valid():
                ing_measurement = ingredientForm.cleaned_data.get('measurement')
                ing_unit = ingredientForm.cleaned_data.get('unit')
                ing_name = ingredientForm.cleaned_data.get('ingredient')

                ingredient = [ing_measurement, ing_unit, ing_name]

                ingredients = request.session['ingredient_array']
                ingredients.append(ingredient)

                request.session['ingredient_array'] = ingredients

        elif 'createIngredient' in request.POST:
            createIngForm = CreateIngredient(request.POST)

            if createIngForm.is_valid():
                model.create_ingredient(createIngForm.cleaned_data.get('ingredientName'))

    template_vars = {
        'recipeInfoForm': recipeInfoForm,
        'addIngredientForm': addIngredientForm,
        'createIngredientForm': createIngredientForm,
        'recipe_name': request.session['recipe_name'],
        'cook_time': request.session['cook_time'],
        'source': request.session['source'],
        'ingredient_array': request.session['ingredient_array'],
    }

    return dmp_render(request, 'newRecipe.ingredients.html', template_vars)

@view_function
def directions(request):

    directionsForm = Directions()

    template_vars = {
        'directionsForm': directionsForm,
        'recipe_name': request.session['recipe_name'],
        'cook_time': request.session['cook_time'],
        'source': request.session['source'],
        'ingredient_array': request.session['ingredient_array'],
    }

    return dmp_render(request, 'newRecipe.directions.html', template_vars)

@view_function
def submit(request):

    if request.method == 'POST':
        directionsForm = Directions(request.POST)
        if directionsForm.is_valid():
            model.add_recipe(request.session['recipe_name'], request.session['cook_time'], request.session['source'], directionsForm.cleaned_data.get('directions'), request.session['ingredient_array'], request.session['meals'])
            recipe = model.Recipe.objects.latest('id')
            ingredients = model.RecipeIngredient.objects.filter(recipe=recipe.id).all()

            request.session.flush()

    template_vars = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    # Redirect to that recipe's detail page
    return dmp_render(request, 'details.html', template_vars)


class RecipeInfo(forms.Form):
    recipeName = forms.CharField(label='Recipe Name', widget=forms.TextInput(attrs={'class': 'form-field'}), required=False)
    cookTime = forms.CharField(label='Total Cook Time', widget=forms.TextInput(attrs={'class': 'form-field'}), required=False)
    source = forms.CharField(label='Recipe Source', widget=forms.TextInput(attrs={'class': 'form-field'}), required=False)
    meals = forms.MultipleChoiceField(label='Meals', choices=model.MEAL_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)

class AddIngredient(forms.Form):
    measurement = forms.DecimalField(label='Measurement', decimal_places=3,  min_value=0, widget=forms.NumberInput(attrs={'class': 'form-field measure'}), required=False)
    unit = forms.ChoiceField(label='Unit', choices=model.UNIT_CHOICES, widget=forms.Select(attrs={'class': 'form-field measure'}), required=False)
    ingredient = forms.ModelChoiceField(queryset=model.Ingredient.objects.all().order_by('ingredient_text'), label='Ingredient', widget=forms.Select(attrs={'class': 'form-field measure'}), required=False)

class CreateIngredient(forms.Form):
    ingredientName = forms.CharField(label='Ingredient Name', widget=forms.TextInput(attrs={'class': 'form-field create'}), required=False)

class Directions(forms.Form):
    directions = forms.CharField(label='Directions', widget=forms.Textarea(attrs={'class': 'form-field'}), required=False)
