# Recipe Calculator
biryani = {
    "Rice": "5kg",
    "OIL": "1/2 kg",
    'spices': "1/4 kg",
    "tomato":"1/4 kg"
}
num_servings = int(input("Enter the number of servings: "))
adjusted_recipe = {}
for ingredient, quantity in biryani.items():
    adjusted_quantity = quantity * num_servings
    adjusted_recipe[ingredient] = adjusted_quantity
print("\nAdjusted Recipe for", num_servings, "servings:")
for ingredient, adjusted_quantity in adjusted_recipe.items():
    print(ingredient + ":", adjusted_quantity)
