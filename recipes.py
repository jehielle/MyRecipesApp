import requests
import textwrap

def show_title():
    # Shows title
    print()
    print("My Recipes Program")
    print()


def show_menu():
    # Shows menu for user
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("0 - Exit the Program")
    print()


def list_categories(categories):
    # Lists the categories
    print("CATEGORIES")
    for i in range(len(categories)):
        category = categories[i]
        print("   " + category.get_category())
    print()


def list_areas(areas):
    print("AREAS:")
    for i in range(len(areas)):
        area = areas[i]
        print("   " + area.get_area())
    print()


def list_meals_by_category(category, meals):
    # Displays list of meals to screen
    # This function works with search_meal_by_category
    print()
    print(category.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print("   " + meal.get_meal())
    print()


def list_meals_by_area(area, meals):
    # Displays list of meals to screen
    print()
    print(area.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print("   " + meal.get_meal())
    print()


def search_meal_by_category(categories):
    # get category name from user and make request to get list
    # This function asks list_meals_by_category to print list
    lookup_category = input("Enter a Category: ")
    found = False

    # validate categories
    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == lookup_category.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals)
    else:
        print("Invalid Category, please try again")


def show_meal_recipe(recipe): #recipe has to be a Recipe object, f is for url
    # Displays meal recipe

    measures = recipe.get_measures()
    ingredients = recipe.get_ingredients()

    print()
    print("Recipe: " + recipe.get_meal())
    print()
    my_wrap = textwrap.TextWrapper(width=80)
    wrap_list = my_wrap.wrap("Instructions: " + recipe.get_instructions())
    for line in wrap_list:
        print(line)
    print()
    print("Ingredients:")
    print("{:20} {:20}".format("Measure", "Ingredient"))
    print("---------------------------------------------")
    for i in range(len(measures)):
        print("{:20} {:20}".format(measures[i], ingredients[i]))
    print()


def search_meal_by_name():
    # gets meal name from user and makes request to print recipe
    lookup_meal = input("Enter Meal Name: ")

    meal_name = requests.get_meal_by_name(lookup_meal)
    if meal_name == False:
        print("Invalid meal name, please try again")
    else:
        show_meal_recipe(meal_name)


def random_meal():
    print("A random meal was selected just for you!")
    recipe = requests.get_random_meal()
    show_meal_recipe(recipe)


def search_meals_by_area(areas):
    lookup_area = input("Enter an Area: ")
    found = False

    for i in range(len(areas)):
        area = areas[i]
        if area.get_area().lower() == lookup_area.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_area(lookup_area)
        list_meals_by_area(lookup_area, meals)
    else:
        print("Invalid area, please try again")


def main():
    show_title()

    # Get list of categories
    categories = requests.get_categories()

    # Get list of areas
    areas = requests.get_areas()

    # User menu selection
    while True:
        show_menu()
        command = input("Command: ")
        if command == "1":
            print()
            list_categories(categories)
        elif command == "2":
            print()
            search_meal_by_category(categories)
        elif command == "3":
            search_meal_by_name()
        elif command == "4":
            random_meal()
        elif command == "5":
            print()
            list_areas(areas)
        elif command == "6":
            search_meals_by_area(areas)
        elif command == "0":
            print("\nThank you for dining with us!\n")
            break
        else:
            print("Not a valid command. Please try again.")
            print()


if __name__ == "__main__":
    main()
