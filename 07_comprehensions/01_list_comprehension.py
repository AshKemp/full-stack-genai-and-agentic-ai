menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [tea for tea in menu if len(tea) < 12]
print(iced_tea)  # Output: ['Iced Lemon

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [num for num in numbers if num%2 == 0]
print("Even numbers: ",even_numbers)