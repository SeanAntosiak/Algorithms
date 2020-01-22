#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_list = list(recipe.keys())
    batches = []
    for item in recipe_list:
        if item in ingredients:
            num = ingredients[item] // recipe[item]
            batches.append(num)
        else:
            return(0)
    lowest_batches = float('inf')
    for num in batches:
        if num < lowest_batches:
            lowest_batches = num
    return(lowest_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
