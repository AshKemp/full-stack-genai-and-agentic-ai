masala_slices = ("cardamom","clove","cinnamon")

(spice1, spice2, spice3) = masala_slices

print(f"Main masala spices are: {spice1}, {spice2}, and {spice3}.")

ginger_ratio, cardamom_ratio = 2,1

print(f"Ratio is G{ginger_ratio} and C{cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio,ginger_ratio
print(f"Ratio is G{ginger_ratio} and C{cardamom_ratio}")

# membership
print(f"Is ginger in masala spices ? {'Cinnamon' in masala_slices}")