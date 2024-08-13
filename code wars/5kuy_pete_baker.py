def can_make_recipe(recipe, available):
    # Initialize the minimum number of times the recipe can be made to a large number
    min_times = float('inf')
    
    # Iterate over each ingredient in the recipe
    for ingredient, amount_needed in recipe.items():
        if ingredient in available:
            amount_available = available[ingredient]
            # Calculate how many times this ingredient allows the recipe to be made
            times = amount_available // amount_needed
            # Update the minimum times if this ingredient is the limiting factor
            if times < min_times:
                min_times = times
        else:
            # If an ingredient is missing, the recipe can't be made even once
            return 0
    
    return min_times