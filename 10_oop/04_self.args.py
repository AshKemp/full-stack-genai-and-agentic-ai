class ChaiCup:
    size = 150 #ml 

    def describe(self):
        return f"A {self.size} ml chai cup."
    
my_cup = ChaiCup()
print(my_cup.describe())  # Output: A 150 ml chai cup.
print(ChaiCup.describe(my_cup))  # Alternative way to call the method

cup_two = ChaiCup()
cup_two.size = 250
print(cup_two.describe())  # Output: A 250 ml chai cup.