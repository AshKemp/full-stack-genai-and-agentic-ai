# def pure_chai(cups):
#     return cups * 10;

# total_chai = 0

# # not recommended
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups * 10
#     return total_chai

# print(pure_chai(2))  # Output: 20
# print(impure_chai(2))  # Output: 20


# def pour_chai(n):
#     print(n)
#     if n == 0:
#         return "All cups are poured"
#     return pour_chai(n-1)

# print("Pouring chai",pour_chai(3))

# chai_types = ["light","kadak","ginger","kadak"]

# strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))

# print(strong_chai)  # Output: ['light', 'ginger']



numbers = [1,2,3,4,5,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x%2 == 0, numbers))

odd_numbers = list(filter(lambda x: x%2 != 0, numbers))

print("Even numbers", even_numbers)
print("Odd numbers", odd_numbers)

