from urllib import request, parse
import json

from objects import Category, Meal, Recipe, Areas

# We will use the open method to make the call
# and retrieve the data from the API.  
# We will then load the data into a JSON object
# from which we can then create our Categories object. 

def get_categories():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories


def get_meals_by_category(category):
    # gets all meals by category
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=' + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])
            meals.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return meals


def get_meal_by_name(meal_name):
    # Gets meal by name
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + parse.quote(meal_name)
    f = request.urlopen(url)

    meal_obj = get_recipe_obj(f)
    if meal_obj == False:
        print("Invalid meal, try again")
    else:
        return meal_obj


def get_random_meal():
    # Gets random meal
    url = 'https://www.themealdb.com/api/json/v1/1/random.php'
    f = request.urlopen(url)

    return get_recipe_obj(f)


def get_recipe_obj(f):
    #Get ingredients & measures
    #Works with get_random_meal and get_meal_by_name
    ingredients = []
    measures = []
    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:

            for i in range(20):
                index = str(i+1)
                if (meal_data['strIngredient' + index] != None 
                    and meal_data['strIngredient' + index] != ""
                    and meal_data['strMeasure' + index] != None 
                    and meal_data['strMeasure' + index] != ""):
                    ingredients.append(meal_data['strIngredient' + index])
                    measures.append(meal_data['strMeasure' + index])
                else:
                    break
                    
            meal_obj = Recipe(meal_data['idMeal'],
                        meal_data['strMeal'],
                        meal_data['strMealThumb'],
                        meal_data['strInstructions'],
                        ingredients,
                        measures)
        return meal_obj #returns one Recipe object

    except (ValueError, KeyError, TypeError):
        return False # will happen if meal does not exist


def get_areas():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for area_data in data['meals']:
            area = Areas(area_data['strArea'])
            areas.append(area)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return areas


def get_meals_by_area(area):
    # gets all meals by category
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            area = Meal(meal_data['idMeal'],
                        meal_data['strMeal'],
                        meal_data['strMealThumb'])
            meals.append(area)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return meals