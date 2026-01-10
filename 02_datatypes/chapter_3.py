# Integer

black_tea_grams = 14
ginger_tea_grams = 3

total_grams = black_tea_grams + ginger_tea_grams
print(f"Total grams of base tea is {total_grams}")

remaining_grams = black_tea_grams - ginger_tea_grams
print(f"Remaining grams of black tea after using ginger tea amount is {remaining_grams}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots 
print(f"Whole tea bags per pot: {bags_per_pot}")

total_cardomom_pods = 10
pods_per_cup = 3
left_over_pods = total_cardomom_pods % pods_per_cup
print(f"Left over cardomom pods after making tea for cups: {left_over_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Powerful flavour strength is: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")