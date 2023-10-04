# This is where we will define all the 
# class objects to make working with the 
# data we get back from the API a little easier.

class Category:
    def __init__(self, category):
        self.__category = category

    def get_category(self):
        return self.__category


class Meal:
    def __init__(self, meal_id, meal, meal_thumb):
        self.__meal_id = meal_id
        self.__meal = meal
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_meal(self):
        return self.__meal
        
    def set_meal(self, meal):
        self.__meal = meal

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


#child of meal
class Recipe(Meal): 
    def __init__(self, meal_id, meal, meal_thumb, instructions, ingredients, measures):
        Meal.__init__(self, meal_id, meal, meal_thumb)
        self.__instructions = instructions
        self.__ingredients = ingredients
        self.__measures = measures

    def get_instructions(self):
        return self.__instructions
    
    def get_ingredients(self):
        return self.__ingredients

    def get_measures(self):
        return self.__measures


class Areas():
    def __init__(self, area):
        self.__area = area

    def get_area(self):
        return self.__area