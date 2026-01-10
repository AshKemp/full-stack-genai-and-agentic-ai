class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature) 

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("Cup size ",cutting.cup)
print("Direct look into the class", Chai.temperature)

del cutting.temperature
del cutting.cup
print("After deleting instance attribute ", cutting.temperature)
print("After deleting instance attribute ", cutting.cup)
print("Direct look into the class", Chai.temperature)