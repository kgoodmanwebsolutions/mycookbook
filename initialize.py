# initialize the django code
print('Initializing Django...')
import sys, os
mydir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(mydir)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mycookbook.settings")
django.setup()

from homepage import models as mod
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
import datetime, random, sys, itertools, glob

print('Initialize File...')

mod.RecipeMeal.objects.all().delete()
mod.RecipeIngredient.objects.all().delete()
mod.Recipe.objects.all().delete()
mod.Ingredient.objects.all().delete()

# Create ingredients
ingredients = []
i = mod.Ingredient()
i.ingredient_text = 'ham'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'pineapple'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'brown sugar'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'tortilla chips'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'salsa'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'sprite'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'lemonade'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'oreos'
ingredients.append(i)
i.save()

i = mod.Ingredient()
i.ingredient_text = 'milk'
ingredients.append(i)
i.save()

# Create recipes
r = mod.Recipe()
r.recipe_name = 'Slow Cooker Ham'
r.source = 'Kristin Goodman'
r.directions = ('Cover the bottom of your crockpot with brown sugar. '
    'Then, you take your ham and place it sliced side down on top of the brown sugar. '
    'Sprinkle a little more brown sugar on top. '
    'Here, you can also add a drained can of pineapple slices, if desired. I didn\'t, because... I don\'t like pineapple! '
    'Cook on low for five hours. '
    'Remove from Crock Pot. '
    'Slice and serve!')
r.cook_time = '5 hours 15 minutes'
r.date_submitted = datetime.datetime.now()
r.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[0]
ri.measurement = '1'
ri.unit = '(No Units)'
ri.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[1]
ri.measurement = '10'
ri.unit = 'Ounces'
ri.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[2]
ri.measurement = '0.5'
ri.unit = 'Cups'
ri.save()

rm = mod.RecipeMeal()
rm.recipe = r
rm.meal = 'Lunch'
rm.save()

rm = mod.RecipeMeal()
rm.recipe = r
rm.meal = 'Dinner'
rm.save()

r = mod.Recipe()
r.recipe_name = 'Chips and Salsa'
r.source = 'Kristin Goodman'
r.directions = ('Put chips and salsa into separate bowls. '
    'Dips chips into salsa and enjoy.')
r.cook_time = '5 minutes'
r.date_submitted = datetime.datetime.now()
r.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[3]
ri.measurement = '15'
ri.unit = 'Ounces'
ri.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[4]
ri.measurement = '1'
ri.unit = 'Cups'
ri.save()

rm = mod.RecipeMeal()
rm.recipe = r
rm.meal = 'Snack'
rm.save()

r = mod.Recipe()
r.recipe_name = '"Spiked" Lemonade'
r.source = 'Kristin Goodman'
r.directions = 'Combine ingredients in a pitcher. Serve with ice.'
r.cook_time = '5 minutes'
r.date_submitted = datetime.datetime.now()
r.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[5]
ri.measurement = '12'
ri.unit = 'Ounces'
ri.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[6]
ri.measurement = '12'
ri.unit = 'Ounces'
ri.save()

rm = mod.RecipeMeal()
rm.recipe = r
rm.meal = 'Beverage'
rm.save()

r = mod.Recipe()
r.recipe_name = 'Oreos and Milk'
r.source = 'Kristin Goodman'
r.directions = ('Pour milk into a glass. '
    'Dip oreos into milk and eat. Drink leftover milk.')
r.cook_time = '5 minutes'
r.date_submitted = datetime.datetime.now()
r.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[7]
ri.measurement = '8'
ri.unit = '(No Units)'
ri.save()

ri = mod.RecipeIngredient()
ri.recipe = r
ri.ingredient = ingredients[8]
ri.measurement = '8'
ri.unit = 'Ounces'
ri.save()

rm = mod.RecipeMeal()
rm.recipe = r
rm.meal = 'Dessert'
rm.save()

print('Initialize complete!')
