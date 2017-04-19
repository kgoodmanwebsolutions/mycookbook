from django.db import models
import datetime

# Create your models here.

MEAL_CHOICES = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Dessert', 'Dessert'),
    ('Snack', 'Snack'),
    ('Beverage', 'Beverage'),
)

UNIT_CHOICES = (
    ('cup', 'Cups'),
    ('tsp', 'Teaspoon'),
    ('tbsp', 'Tablespoon'),
    ('oz', 'Ounces'),
    ('', '(No Units)'),
)

class Ingredient(models.Model):
    ingredient_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ingredient_text

class Recipe(models.Model):
    recipe_name = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    date_submitted = models.DateField(null=True, blank=True)
    cook_time = models.TextField(null=True, blank=True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    measurement = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=3)
    unit = models.TextField(null=True, blank=True, choices=UNIT_CHOICES)

class RecipeMeal(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    meal = models.TextField(null=True, blank=True)

def create_ingredient(ing_text):
    if not Ingredient.objects.filter(ingredient_text=ing_text).exists():
        i = Ingredient()
        i.ingredient_text = ing_text
        i.save()

def add_recipe(recipe_name, cook_time, source, directions, ingredient_array, meal_list):
    r = Recipe()
    r.recipe_name = recipe_name
    r.source = source
    r.directions = directions
    r.cook_time = cook_time
    r.date_submitted = datetime.datetime.now()
    r.save()

    for item in meal_list:
        rm = RecipeMeal()
        rm.recipe = r
        rm.meal = item
        rm.save()

    for item in ingredient_array:
        # CHECK IF ALREADY IN DATABASE

        ri = RecipeIngredient()
        ri.recipe = r
        ri.ingredient = item[2]
        ri.measurement = item[0]
        ri.unit = item[1]
        ri.save()
