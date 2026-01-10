class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# creating objects out of the class

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False
print(f"Masala Class: ",masala.is_hot)
print(f"Class: ",Chai.is_hot)

masala.flavor = "Masala"
print(masala.flavor)