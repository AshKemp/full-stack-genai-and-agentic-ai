ingredients = ["water","milk","black tea"]

print(f"Initial ingredients: {ingredients}")
ingredients.append("sugar")
print(f"Ingredients after adding sugar: {ingredients}")
ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"Final chai ingredients: {chai_ingredients}")

chai_ingredients.insert(2,"black tea")
print(f"Chai ingredients after inserting milk: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Chai ingredients after popping last item ({last_added}): {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai ingredients after reversing: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water","milk"]

extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea","water"] * 3
print(f"Strong brew ingredients: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Raw spice data: {raw_spice_data}")